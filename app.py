import streamlit as st

from graph.workflow import build_graph
from state.schemas import AcquisitionState


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="M&A Intelligence",
    page_icon="📊",
    layout="wide"
)


# ============================================================
# HEADER
# ============================================================

st.html(
    """
    <div style="
        padding: 1.5rem 2rem;
        border-radius: 12px;
        background: linear-gradient(135deg, #1f2937, #111827);
        margin-bottom: 2rem;
    ">
        <h1 style="
            margin: 0;
            color: white;
            font-size: 2.4rem;
        ">
            M&A Intelligence
        </h1>

        <p style="
            margin-top: 0.5rem;
            margin-bottom: 0;
            color: #d1d5db;
            font-size: 1.1rem;
        ">
            Autonomous Acquisition Due-Diligence Platform
        </p>

        <p style="
            margin-top: 0.8rem;
            margin-bottom: 0;
            color: #9ca3af;
        ">
            AI-powered multi-agent analysis for strategic,
            financial, regulatory, and operational due diligence.
        </p>
    </div>
    """
)


# ============================================================
# INPUT SECTION
# ============================================================

st.divider()

st.header("Acquisition Analysis")

col1, col2 = st.columns(2)

with col1:

    company_a = st.text_input(
        "Acquiring Company",
        placeholder="e.g., Microsoft"
    )

with col2:

    company_b = st.text_input(
        "Target Company",
        placeholder="e.g., OpenAI"
    )


user_question = st.text_area(
    "Acquisition Question",
    placeholder="e.g., Should Microsoft acquire OpenAI?",
    height=100
)


analyze = st.button(
    "Run Acquisition Analysis",
    type="primary"
)


# ============================================================
# RUN WORKFLOW
# ============================================================

if analyze:

    if not company_a or not company_b or not user_question:

        st.warning(
            "Please provide the acquiring company, target company, "
            "and acquisition question."
        )

    else:

        initial_state = AcquisitionState(
            company_a=company_a,
            company_b=company_b,
            user_question=user_question
        )

        try:

            with st.spinner(
                "Running M&A due-diligence workflow..."
            ):

                graph = build_graph()

                result = graph.invoke(initial_state)

            st.success(
                "Acquisition analysis completed successfully."
            )

            # ====================================================
            # ACQUISITION SUMMARY
            # ====================================================

            st.write("### Acquisition")

            st.write(
                f"**{company_a} → {company_b}**"
            )

            st.write(
                f"**Question:** {user_question}"
            )


            # ====================================================
            # FINAL RECOMMENDATION
            # ====================================================

            recommendation = result.get("committee_decision")

            if recommendation is None:

                recommendation = result.get(
                    "final_recommendation"
                )


            if recommendation is not None:

                st.divider()

                st.header("Final Recommendation")

                col1, col2 = st.columns([3, 1])

                with col1:

                    st.subheader(
                        recommendation.recommendation
                    )

                with col2:

                    st.metric(
                        "Confidence",
                        recommendation.confidence
                    )


                # -----------------------------------------------
                # STRATEGIC RATIONALE
                # -----------------------------------------------

                st.write("### Strategic Rationale")

                st.write(
                    recommendation.strategic_rationale
                )


                # -----------------------------------------------
                # FINANCIAL ASSESSMENT
                # -----------------------------------------------

                st.write("### Financial Assessment")

                st.write(
                    recommendation.financial_assessment
                )


                # -----------------------------------------------
                # VALUATION ASSESSMENT
                # -----------------------------------------------

                st.write("### Valuation Assessment")

                st.write(
                    recommendation.valuation_assessment
                )


                # -----------------------------------------------
                # KEY OPPORTUNITIES
                # -----------------------------------------------

                st.write("### Key Opportunities")

                for opportunity in recommendation.key_opportunities:

                    st.write(
                        f"- {opportunity}"
                    )


                # -----------------------------------------------
                # KEY RISKS
                # -----------------------------------------------

                st.write("### Key Risks")

                for risk in recommendation.key_risks:

                    st.write(
                        f"- {risk}"
                    )


                # -----------------------------------------------
                # REGULATORY CONCERNS
                # -----------------------------------------------

                st.write("### Regulatory Concerns")

                for concern in recommendation.regulatory_concerns:

                    st.write(
                        f"- {concern}"
                    )


                # -----------------------------------------------
                # INTEGRATION CONCERNS
                # -----------------------------------------------

                st.write("### Integration Concerns")

                for concern in recommendation.integration_concerns:

                    st.write(
                        f"- {concern}"
                    )


                # -----------------------------------------------
                # CONDITIONS BEFORE ACQUISITION
                # -----------------------------------------------

                st.write(
                    "### Conditions Before Acquisition"
                )

                for condition in recommendation.conditions_before_acquisition:

                    st.write(
                        f"- {condition}"
                    )


            else:

                st.warning(
                    "The workflow completed, but no final "
                    "recommendation was returned."
                )


            # ====================================================
            # EVIDENCE
            # ====================================================

            evidence_list = result.get("evidence", [])


            if evidence_list:

                st.divider()

                st.header("Evidence")

                st.write(
                    "Sources and extracted evidence supporting "
                    "the acquisition analysis."
                )


                # ------------------------------------------------
                # FINAL DEDUPLICATION
                # ------------------------------------------------

                unique_evidence = {}

                for evidence in evidence_list:

                    evidence_id = getattr(
                        evidence,
                        "evidence_id",
                        None
                    )

                    if evidence_id:

                        unique_evidence[
                            evidence_id
                        ] = evidence


                evidence_list = list(
                    unique_evidence.values()
                )


                # ------------------------------------------------
                # DISPLAY EVIDENCE
                # ------------------------------------------------

                st.caption(
                    f"{len(evidence_list)} unique evidence sources"
                )


                for evidence in evidence_list:

                    title = (
                        evidence.title
                        if evidence.title
                        else evidence.source_name
                    )


                    with st.expander(
                        f"{evidence.evidence_id} — {title}"
                    ):

                        st.write(
                            f"**Source:** "
                            f"{evidence.source_name}"
                        )

                        st.write(
                            f"**Source Type:** "
                            f"{evidence.source_type}"
                        )

                        st.write(
                            f"**Credibility:** "
                            f"{evidence.credibility}"
                        )


                        if evidence.published_at:

                            st.write(
                                f"**Published:** "
                                f"{evidence.published_at}"
                            )


                        if evidence.title:

                            st.write(
                                f"**Title:** "
                                f"{evidence.title}"
                            )


                        st.write("### Evidence")

                        # Handle dictionaries / lists cleanly
                        if isinstance(
                            evidence.content,
                            (dict, list)
                        ):

                            st.json(
                                evidence.content
                            )

                        else:

                            st.write(
                                evidence.content
                            )


                        st.write("### Relevance")

                        st.write(
                            evidence.relevance
                        )


                        if evidence.url:

                            st.markdown(
                                f"[View Source]({evidence.url})"
                            )


            else:

                st.info(
                    "No evidence was returned by the workflow."
                )


        # ========================================================
        # ERROR HANDLING
        # ========================================================

        except Exception as e:

            st.error(
                "An error occurred while running the "
                "acquisition analysis."
            )

            st.exception(e)