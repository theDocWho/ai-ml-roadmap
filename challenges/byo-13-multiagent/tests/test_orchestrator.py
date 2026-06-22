"""Staged acceptance tests for BYO-13. Deterministic mock agents, fully offline."""
from multiagent.orchestrator import Orchestrator


# ----- Stage 1: message bus + shared state -----
def test_stage1_messages_logged_in_order():
    orch = Orchestrator([("a1", lambda s: {"x": 1}), ("a2", lambda s: {"y": 2})], max_rounds=1)
    final = orch.run({}, stop_when=lambda s: False)
    assert [name for name, _ in final["messages"]] == ["a1", "a2"]
    assert final["x"] == 1 and final["y"] == 2          # updates merged into shared state


def test_stage1_does_not_mutate_caller_state():
    init = {}
    orch = Orchestrator([("a", lambda s: {"v": 1})], max_rounds=1)
    orch.run(init, stop_when=lambda s: False)
    assert init == {}                                   # caller's dict untouched


# ----- Stage 2: planner -> worker -> critic reaches a goal -----
def test_stage2_pipeline_reaches_goal():
    def planner(s):
        return {"plan": ["a", "b"], "done": []} if "plan" not in s else {}

    def worker(s):
        plan, done = s.get("plan", []), s.get("done", [])
        return {"done": done + [plan[len(done)]]} if len(done) < len(plan) else {}

    def critic(s):
        plan, done = s.get("plan", []), s.get("done", [])
        return {"approved": len(plan) > 0 and len(done) == len(plan)}

    orch = Orchestrator([("planner", planner), ("worker", worker), ("critic", critic)],
                        max_rounds=10)
    final = orch.run({}, stop_when=lambda s: s.get("approved", False))
    assert final["approved"] is True
    assert final["done"] == ["a", "b"]


# ----- Stage 3: max_rounds safety -----
def test_stage3_max_rounds_terminates():
    orch = Orchestrator([("noop", lambda s: {})], max_rounds=3)
    final = orch.run({}, stop_when=lambda s: False)
    assert len(final["messages"]) == 3                  # 1 agent x 3 rounds, then stop
