from langgraph.graph import END, START, StateGraph

from agents.financial import financial_node
from agents.planner import planner_node
from agents.market import market_node
from state.schemas import AcquisitionState


def build_graph():

    builder = StateGraph(AcquisitionState)

    builder.add_node("planner", planner_node)
    builder.add_node("financial", financial_node)
    builder.add_node("market", market_node)
    
    builder.add_edge(START, "planner")
    builder.add_edge("planner", "financial")
    builder.add_edge("financial", "market")
    builder.add_edge("market", END)

    return builder.compile()