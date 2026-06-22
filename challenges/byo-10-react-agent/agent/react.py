"""BYO-10 starter — a ReAct (Reason + Act) agent loop from scratch (stdlib only).

The LLM is **injected** as a callable `prompt -> str`; tools are a dict `name -> callable`. Tests
pass a scripted mock LLM and mock tools, so the loop is fully deterministic and offline. This is the
core control loop behind every tool-using agent. See README.md.
"""
import re


def parse_action(text):
    """Stage 1: pull a tool call out of an LLM step. Looks for lines:
        Action: <tool name>
        Action Input: <argument>
    Return (tool_name, tool_input) stripped, or None if not both present."""
    raise NotImplementedError("implement parse_action")


def parse_final(text):
    """Stage 1: if the text contains 'Final Answer: <x>', return <x> (stripped); else None."""
    raise NotImplementedError("implement parse_final")


class ReActAgent:
    def __init__(self, tools, llm, max_steps=5):
        self.tools = tools          # dict: name -> callable(str) -> str
        self.llm = llm              # callable: prompt -> str
        self.max_steps = max_steps

    def run(self, question):
        """Stage 2-3: the ReAct loop.
        Keep a `scratchpad` string. Up to max_steps times:
          1. prompt = f"Question: {question}\n{scratchpad}"
          2. step = self.llm(prompt)
          3. if parse_final(step) is not None: return it.
          4. else parse_action(step) -> (tool, arg); run obs = self.tools[tool](arg).
          5. append f"{step}\nObservation: {obs}\n" to the scratchpad.
        Return None if no Final Answer within max_steps (prevents infinite loops)."""
        raise NotImplementedError("implement ReActAgent.run")
