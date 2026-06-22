"""Staged acceptance tests for BYO-10. Fully offline: scripted LLM + mock tools."""
from agent.react import parse_action, parse_final, ReActAgent


class ScriptedLLM:
    """A deterministic stand-in for an LLM: returns pre-written steps in order."""
    def __init__(self, steps):
        self.steps = steps
        self.i = 0

    def __call__(self, prompt):
        out = self.steps[min(self.i, len(self.steps) - 1)]
        self.i += 1
        return out


def calculator(expr):
    return str(eval(expr, {"__builtins__": {}}))     # safe: no builtins


# ----- Stage 1: parsing -----
def test_stage1_parse_action():
    assert parse_action("Thought: I should compute\nAction: calculator\nAction Input: 2 + 3") == (
        "calculator", "2 + 3")
    assert parse_action("Final Answer: 5") is None


def test_stage1_parse_final():
    assert parse_final("Thought: done\nFinal Answer: 42") == "42"
    assert parse_final("Action: x\nAction Input: y") is None


# ----- Stage 2/3: the loop -----
def test_stage23_agent_uses_tool_then_finishes():
    agent = ReActAgent(
        tools={"calculator": calculator},
        llm=ScriptedLLM([
            "Thought: compute it\nAction: calculator\nAction Input: 2 + 3",
            "Thought: I have it\nFinal Answer: 5",
        ]),
    )
    assert agent.run("what is 2 + 3?") == "5"


def test_stage23_multi_tool_sequence():
    calls = []

    def echo(x):
        calls.append(x)
        return x.upper()

    agent = ReActAgent(
        tools={"echo": echo},
        llm=ScriptedLLM([
            "Action: echo\nAction Input: hello",
            "Action: echo\nAction Input: world",
            "Final Answer: done",
        ]),
    )
    assert agent.run("q") == "done"
    assert calls == ["hello", "world"]      # both tool calls executed in order


def test_stage3_max_steps_prevents_infinite_loop():
    agent = ReActAgent(
        tools={"noop": lambda x: "ok"},
        llm=ScriptedLLM(["Action: noop\nAction Input: a"]),   # never returns Final Answer
        max_steps=3,
    )
    assert agent.run("q") is None
