from langgraph.graph import END, START, StateGraph

from agents.financial import financial_node
from agents.planner import planner_node
from agents.market import market_node
from agents.competitive import competitive_node
from agents.legal import legal_node
from agents.regulatory import regulatory_node
from agents.risk import risk_node
from agents.valuation import valuation_node
from agents.integration import integration_node
from agents.stakeholder import stakeholder_node
from agents.critic import critic_node
from agents.synergy import synergy_node
from agents.committee import committee_node
from state.schemas import AcquisitionState


# ==========================================
# AGGREGATOR NODE
# ==========================================

def aggregator_node(state: AcquisitionState):

    print("\n>>> AGGREGATOR NODE STARTED")

    print(
        f">>> Evidence collected: "
        f"{len(state.evidence)}"
    )

    print(
        f">>> Financial findings: "
        f"{len(state.financial_findings)}"
    )

    print(
        f">>> Market findings: "
        f"{len(state.market_findings)}"
    )

    print(
        f">>> Competitive findings: "
        f"{len(state.competitor_findings)}"
    )

    print(
        f">>> Legal findings: "
        f"{len(state.legal_findings)}"
    )

    print(
        f">>> Regulatory findings: "
        f"{len(state.regulatory_findings)}"
    )

    print(
        f">>> Risk findings: "
        f"{len(state.risks)}"
    )

    print(
        f">>> Integration findings: "
        f"{len(state.integration_findings)}"
    )

    print(
        f">>> Stakeholder findings: "
        f"{len(state.stakeholder_findings)}"
    )

    print(
        f">>> Synergy findings: "
        f"{len(state.synergies)}"
    )

    print(
        f">>> Valuation available: "
        f"{state.valuation is not None}"
    )

    print(">>> AGGREGATOR NODE COMPLETED")

    # The specialist agents now write their evidence
    # directly into state.evidence.
    #
    # Therefore, the aggregator acts only as a
    # synchronization/checkpoint node.
    #
    # Returning an empty dictionary means that the
    # aggregator does not modify any state fields.

    return {}


# ==========================================
# CRITIC ROUTER
# ==========================================

def critic_router(state: AcquisitionState):

    latest_feedback = state.critic_feedback[-1]

    if latest_feedback.approved:
        return "end"

    if state.revision_count >= 2:
        return "end"

    return "revise"


# ==========================================
# BUILD GRAPH
# ==========================================

def build_graph():

    graph = StateGraph(AcquisitionState)

    # ==========================================
    # NODES
    # ==========================================

    graph.add_node(
        "planner",
        planner_node
    )

    graph.add_node(
        "financial",
        financial_node
    )

    graph.add_node(
        "market",
        market_node
    )

    graph.add_node(
        "competitive",
        competitive_node
    )

    graph.add_node(
        "legal",
        legal_node
    )

    graph.add_node(
        "regulatory",
        regulatory_node
    )

    graph.add_node(
        "risk",
        risk_node
    )

    graph.add_node(
        "valuation",
        valuation_node
    )

    graph.add_node(
        "integration",
        integration_node
    )

    graph.add_node(
        "stakeholder",
        stakeholder_node
    )

    graph.add_node(
        "synergy",
        synergy_node
    )

    graph.add_node(
        "aggregator",
        aggregator_node
    )

    graph.add_node(
        "committee",
        committee_node
    )

    graph.add_node(
        "critic",
        critic_node
    )

    # ==========================================
    # RESEARCH FLOW
    # ==========================================

    graph.add_edge(
        START,
        "planner"
    )

    graph.add_edge(
        "planner",
        "financial"
    )

    graph.add_edge(
        "planner",
        "market"
    )

    graph.add_edge(
        "planner",
        "competitive"
    )

    graph.add_edge(
        "planner",
        "legal"
    )

    graph.add_edge(
        "planner",
        "regulatory"
    )

    graph.add_edge(
        "planner",
        "risk"
    )

    graph.add_edge(
        "planner",
        "valuation"
    )

    graph.add_edge(
        "planner",
        "integration"
    )

    graph.add_edge(
        "planner",
        "stakeholder"
    )

    graph.add_edge(
        "planner",
        "synergy"
    )

    # ==========================================
    # AGGREGATION / SYNCHRONIZATION
    # ==========================================

    graph.add_edge(
        "financial",
        "aggregator"
    )

    graph.add_edge(
        "market",
        "aggregator"
    )

    graph.add_edge(
        "competitive",
        "aggregator"
    )

    graph.add_edge(
        "legal",
        "aggregator"
    )

    graph.add_edge(
        "regulatory",
        "aggregator"
    )

    graph.add_edge(
        "risk",
        "aggregator"
    )

    graph.add_edge(
        "valuation",
        "aggregator"
    )

    graph.add_edge(
        "integration",
        "aggregator"
    )

    graph.add_edge(
        "stakeholder",
        "aggregator"
    )

    graph.add_edge(
        "synergy",
        "aggregator"
    )

    # ==========================================
    # COMMITTEE
    # ==========================================

    graph.add_edge(
        "aggregator",
        "committee"
    )

    # ==========================================
    # CRITIC
    # ==========================================

    graph.add_edge(
        "committee",
        "critic"
    )

    # ==========================================
    # CRITIC ROUTING
    # ==========================================

    graph.add_conditional_edges(
        "critic",
        critic_router,
        {
            "revise": "committee",
            "end": END,
        }
    )

    return graph.compile()