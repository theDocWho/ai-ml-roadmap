"""BYO-13 starter — a multi-agent orchestrator from scratch (stdlib only). See README.md.

Agents are plain callables `agent(state) -> dict` (a state update). The orchestrator runs them in
rounds over a **shared state** ("blackboard"), logs every message, and stops when a goal predicate
is met. Tests use deterministic mock agents (planner / worker / critic), so it's fully offline.
"""


class Orchestrator:
    def __init__(self, agents, max_rounds=5):
        # agents: list of (name, callable(state) -> dict of state updates)
        self.agents = agents
        self.max_rounds = max_rounds

    def run(self, initial_state, stop_when):
        """Run up to max_rounds. Each round, for each (name, agent):
          1. update = agent(state)
          2. append (name, update) to state['messages']   (the message bus / log)
          3. merge update into the shared state
          4. if stop_when(state): return state immediately
        Initialize state from a copy of initial_state with an empty 'messages' list.
        Return the final state (even if the goal was never met)."""
        raise NotImplementedError("implement Orchestrator.run")
