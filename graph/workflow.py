from langgraph.graph import END, START, StateGraph

from agents.planner import planner_node
from state.schemas import AcquisitionState


def build_graph():

    builder = StateGraph(AcquisitionState)

    builder.add_node("planner", planner_node)

    builder.add_edge(START, "planner")
    builder.add_edge("planner", END)

    return builder.compile()