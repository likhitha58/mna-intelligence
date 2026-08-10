from langgraph.graph import END, START, StateGraph

from agents.financial import financial_node
from agents.planner import planner_node
from agents.market import market_node
from state.schemas import AcquisitionState
from agents.competitive import competitive_node

def aggregator_node(state):
    return {}

def build_graph():

    graph = StateGraph(AcquisitionState)

    graph.add_node("planner", planner_node)
    graph.add_node("financial", financial_node)
    graph.add_node("market", market_node)
    graph.add_node("aggregator", aggregator_node)
    graph.add_node(
    "competitive",
    competitive_node
    )
    graph.add_edge(START, "planner")

    graph.add_edge("planner", "financial")
    graph.add_edge("planner", "market")

    graph.add_edge("financial", "aggregator")
    graph.add_edge("market", "aggregator")
    graph.add_edge(
    "planner",
    "competitive"
    )
    graph.add_edge(
    "competitive",
    "aggregator"
    )
    graph.add_edge("aggregator", END)

    return graph.compile()