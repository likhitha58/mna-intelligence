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
# from agents.decision import decision_node
from agents.critic import critic_node
from agents.synergy import synergy_node
from agents.committee import committee_node
from state.schemas import AcquisitionState


def aggregator_node(state: AcquisitionState):

    print("\n>>> AGGREGATOR NODE STARTED")

    evidence = []

    all_findings = [
        ("financial", state.financial_findings),
        ("market", state.market_findings),
        ("competitive", state.competitor_findings),
        ("legal", state.legal_findings),
        ("regulatory", state.regulatory_findings),
        ("risk", state.risks),
        ("valuation", [state.valuation] if state.valuation else []),
        ("integration", state.integration_findings),
        ("stakeholder", state.stakeholder_findings),
        ("synergy", state.synergies),
    ]

    for agent_name, findings in all_findings:

        print(
            f"\n>>> {agent_name.upper()} FINDINGS: "
            f"{len(findings)}"
        )

        for finding in findings:

            print(
                f">>> {agent_name.upper()} FINDING TYPE: "
                f"{type(finding).__name__}"
            )

            if hasattr(finding, "evidence"):

                print(
                    f">>> {agent_name.upper()} EVIDENCE COUNT: "
                    f"{len(finding.evidence)}"
                )

                evidence.extend(finding.evidence)

            else:

                print(
                    f">>> {agent_name.upper()} HAS NO EVIDENCE FIELD"
                )

    # ==========================================
    # REMOVE DUPLICATES
    # ==========================================

    unique_evidence = {}

    for item in evidence:

        if hasattr(item, "evidence_id"):

            unique_evidence[item.evidence_id] = item

    evidence = list(unique_evidence.values())

    print(
        f"\n>>> TOTAL EVIDENCE BEFORE DEDUPLICATION: "
        f"{len(evidence)}"
    )

    print(
        f">>> UNIQUE EVIDENCE COUNT: "
        f"{len(evidence)}"
    )

    print(">>> AGGREGATOR NODE COMPLETED")

    return {
        "evidence": evidence
    }


def critic_router(state: AcquisitionState):

    latest_feedback = state.critic_feedback[-1]

    if latest_feedback.approved:
        return "end"

    if state.revision_count >= 2:
        return "end"

    return "revise"


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
        "aggregator",
        aggregator_node
    )

    graph.add_node(
        "critic",
        critic_node
    )
    graph.add_node("synergy", synergy_node)
    
    graph.add_node(
    "committee",
    committee_node
    )

    # ==========================================
    # RESEARCH FLOW
    # ==========================================

    graph.add_edge(
        START,
        "planner"
    )

    graph.add_edge("planner", "financial")
    graph.add_edge("planner", "market")
    graph.add_edge("planner", "competitive")
    graph.add_edge("planner", "legal")
    graph.add_edge("planner", "regulatory")
    graph.add_edge("planner", "risk")
    graph.add_edge("planner", "valuation")
    graph.add_edge("planner", "integration")
    graph.add_edge("planner", "stakeholder")
    graph.add_edge("planner", "synergy")

    # ==========================================
    # AGGREGATION
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
    graph.add_edge("synergy", "aggregator")

    # ==========================================
    # DECISION
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