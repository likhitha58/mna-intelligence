from langgraph.graph import END, START, StateGraph

from agents.financial import financial_node
from agents.planner import planner_node
from agents.market import market_node
from state.schemas import AcquisitionState
from agents.competitive import competitive_node
from agents.legal import legal_node
from agents.regulatory import regulatory_node
from agents.risk import risk_node
from agents.valuation import valuation_node
from agents.integration import integration_node
from agents.stakeholder import stakeholder_node
from agents.decision import decision_node
from agents.critic import critic_node

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
    graph.add_node(
    "legal",
    legal_node
    )
    graph.add_node("regulatory", regulatory_node)
    graph.add_node(
    "risk",
    risk_node
    )
    graph.add_node("valuation", valuation_node)
    graph.add_node(
    "integration",
    integration_node
    )
    graph.add_node(
    "stakeholder",
    stakeholder_node
    )
    graph.add_node("critic", critic_node)
    graph.add_node("decision", decision_node)
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
    graph.add_edge(
    "planner",
    "legal"
    )
    graph.add_edge(
    "legal",
    "aggregator"
    )
    graph.add_edge(
    "planner",
    "regulatory"
    )
    graph.add_edge(
    "regulatory",
    "aggregator"
    )
    graph.add_edge(
    "planner",
    "risk"
    )
    graph.add_edge(
    "risk",
    "aggregator"
    )
    graph.add_edge("planner", "valuation")
    graph.add_edge("valuation", "aggregator")
    graph.add_edge(
    "planner",
    "integration"
    )
    graph.add_edge(
    "integration",
    "aggregator"
    )
    graph.add_edge(
    "planner",
    "stakeholder"
    )

    graph.add_edge(
        "stakeholder",
        "aggregator"
    )
    graph.add_edge("aggregator", "decision")
    graph.add_edge("decision", "critic")
    graph.add_edge("critic", END)

    return graph.compile()