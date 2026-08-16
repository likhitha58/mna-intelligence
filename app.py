import streamlit as st
from graph.workflow import build_graph
from state.schemas import AcquisitionState


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="M&A Intelligence",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.html(
    """
    <style>

    /* ------------------------------
       GLOBAL
    ------------------------------ */

    .main {
        background-color: #f8fafc;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1500px;
    }


    /* ------------------------------
       HEADER
    ------------------------------ */

    .hero {
        padding: 2rem 2.5rem;
        border-radius: 18px;
        background:
            linear-gradient(
                135deg,
                #111827 0%,
                #1e293b 55%,
                #334155 100%
            );
        box-shadow: 0 10px 30px rgba(15, 23, 42, 0.15);
        margin-bottom: 2rem;
    }

    .hero-title {
        color: white;
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 0.4rem;
    }

    .hero-subtitle {
        color: #cbd5e1;
        font-size: 1.1rem;
        margin-bottom: 0.7rem;
    }

    .hero-description {
        color: #94a3b8;
        font-size: 0.95rem;
    }


    /* ------------------------------
       CARDS
    ------------------------------ */

    .card {
        background: white;
        padding: 1.5rem;
        border-radius: 16px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 4px 15px rgba(15, 23, 42, 0.05);
        margin-bottom: 1rem;
    }

    .card-title {
        font-size: 1.05rem;
        font-weight: 700;
        color: #0f172a;
        margin-bottom: 0.6rem;
    }

    .card-text {
        color: #475569;
        line-height: 1.65;
    }


    /* ------------------------------
       RECOMMENDATION
    ------------------------------ */

    .recommendation-card {
        background:
            linear-gradient(
                135deg,
                #ffffff,
                #f8fafc
            );
        padding: 2rem;
        border-radius: 18px;
        border: 1px solid #cbd5e1;
        box-shadow: 0 8px 25px rgba(15, 23, 42, 0.08);
        margin: 1rem 0 1.5rem 0;
    }

    .recommendation-label {
        color: #64748b;
        font-size: 0.8rem;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        font-weight: 700;
    }

    .recommendation-value {
        color: #0f172a;
        font-size: 2rem;
        font-weight: 750;
        margin-top: 0.3rem;
    }


    /* ------------------------------
       SECTION HEADERS
    ------------------------------ */

    .section-title {
        color: #0f172a;
        font-size: 1.45rem;
        font-weight: 700;
        margin-top: 1.5rem;
        margin-bottom: 1rem;
    }


    /* ------------------------------
       TAGS
    ------------------------------ */

    .tag {
        display: inline-block;
        padding: 0.35rem 0.7rem;
        margin: 0.2rem;
        border-radius: 999px;
        background: #f1f5f9;
        color: #334155;
        font-size: 0.8rem;
        font-weight: 600;
    }


    /* ------------------------------
       SIDEBAR
    ------------------------------ */

    section[data-testid="stSidebar"] {
        background-color: #0f172a;
    }

    section[data-testid="stSidebar"] * {
        color: #e2e8f0;
    }


    /* ------------------------------
       METRICS
    ------------------------------ */

    div[data-testid="stMetric"] {
        background: white;
        border: 1px solid #e2e8f0;
        padding: 1rem;
        border-radius: 14px;
        box-shadow: 0 3px 12px rgba(15, 23, 42, 0.04);
    }


    /* ------------------------------
       BUTTONS
    ------------------------------ */

    .stButton > button {
        border-radius: 10px;
        font-weight: 600;
        min-height: 2.7rem;
    }

    </style>
    """
)


# ============================================================
# HERO HEADER
# ============================================================

st.html(
    """
    <div class="hero">

        <div class="hero-title">
            📊 M&A Intelligence
        </div>

        <div class="hero-subtitle">
            Autonomous Acquisition Due-Diligence Platform
        </div>

        <div class="hero-description">
            Multi-agent intelligence for strategic, financial,
            regulatory, competitive, legal and operational
            acquisition analysis.
        </div>

    </div>
    """
)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown("## Acquisition Setup")

    st.caption(
        "Define the transaction you want the M&A intelligence "
        "system to evaluate."
    )

    company_a = st.text_input(
        "Acquiring Company",
        placeholder="Microsoft"
    )

    company_b = st.text_input(
        "Target Company",
        placeholder="OpenAI"
    )

    user_question = st.text_area(
        "Acquisition Question",
        placeholder="Should Microsoft acquire OpenAI?",
        height=120
    )

    st.divider()

    analyze = st.button(
        "🚀 Run Acquisition Analysis",
        type="primary",
        use_container_width=True
    )

    reset = st.button(
        "↻ Reset",
        use_container_width=True
    )

    if reset:
        st.session_state.pop("analysis_result", None)
        st.rerun()

    st.divider()

    st.caption("M&A Intelligence Platform")
    st.caption("Multi-Agent Due Diligence")


# ============================================================
# MAIN INPUT VALIDATION
# ============================================================

if analyze:

    if not company_a.strip() or not company_b.strip() or not user_question.strip():

        st.warning(
            "Please provide the acquiring company, target company, "
            "and acquisition question."
        )

    else:

        initial_state = AcquisitionState(
            company_a=company_a.strip(),
            company_b=company_b.strip(),
            user_question=user_question.strip()
        )

        # ----------------------------------------------------
        # RUN GRAPH
        # ----------------------------------------------------

        with st.status(
            "Running M&A due-diligence workflow...",
            expanded=True
        ) as status:

            st.write("🔎 Running research agents...")
            st.write("📊 Analyzing financial and valuation factors...")
            st.write("⚖️ Evaluating legal and regulatory risks...")
            st.write("🤝 Evaluating strategic synergies...")
            st.write("🧠 Generating committee recommendation...")
            st.write("🔍 Running critic review...")

            graph = build_graph()

            result = graph.invoke(initial_state)

            status.update(
                label="M&A analysis completed",
                state="complete",
                expanded=False
            )

        st.session_state["analysis_result"] = result


# ============================================================
# LOAD STORED RESULT
# ============================================================

result = st.session_state.get("analysis_result")


# ============================================================
# EMPTY STATE
# ============================================================

if result is None:

    st.html(
        """
        <div class="card">

        <div class="card-title">
            Welcome to M&A Intelligence
        </div>

        <div class="card-text">

        Enter an acquiring company, target company and
        acquisition question from the sidebar to begin
        autonomous acquisition due diligence.

        The system evaluates:

        </div>

        <br>

        <span class="tag">Financial</span>
        <span class="tag">Valuation</span>
        <span class="tag">Competitive</span>
        <span class="tag">Legal</span>
        <span class="tag">Regulatory</span>
        <span class="tag">Risk</span>
        <span class="tag">Integration</span>
        <span class="tag">Stakeholder</span>
        <span class="tag">Synergy</span>

        </div>
        """
    )

    st.stop()


# ============================================================
# NORMALIZE RESULT
# ============================================================

if hasattr(result, "model_dump"):
    result = result.model_dump()


# ============================================================
# ACQUISITION SUMMARY
# ============================================================

st.markdown(
    '<div class="section-title">Acquisition Overview</div>',
    unsafe_allow_html=True
)

overview_col1, overview_col2, overview_col3 = st.columns(3)

with overview_col1:

    st.metric(
        "Acquirer",
        company_a or result.get("company_a", "N/A")
    )

with overview_col2:

    st.metric(
        "Target",
        company_b or result.get("company_b", "N/A")
    )

with overview_col3:

    evidence_count = len(
        result.get("evidence", []) or []
    )

    st.metric(
        "Evidence Items",
        evidence_count
    )


st.markdown(
    f"""
    <div class="card">

    <div class="card-title">
        Acquisition Question
    </div>

    <div class="card-text">
        {user_question or result.get("user_question", "N/A")}
    </div>

    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# COMMITTEE DECISION
# ============================================================

recommendation = result.get("final_recommendation")

if recommendation is None:

    recommendation = result.get("committee_decision")


if recommendation is not None:

    if hasattr(recommendation, "model_dump"):
        recommendation = recommendation.model_dump()

    st.markdown(
        '<div class="section-title">Executive Recommendation</div>',
        unsafe_allow_html=True
    )

    rec_col1, rec_col2 = st.columns([4, 1])

    with rec_col1:

        st.markdown(
            f"""
            <div class="recommendation-card">

                <div class="recommendation-label">
                    Recommended Decision
                </div>

                <div class="recommendation-value">
                    {recommendation.get("recommendation", "N/A")}
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    with rec_col2:

        st.metric(
            "Confidence",
            recommendation.get(
                "confidence",
                "N/A"
            )
        )


    # ========================================================
    # STRATEGIC RATIONALE
    # ========================================================

    st.markdown(
        '<div class="section-title">Strategic Rationale</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div class="card">

        <div class="card-text">

        {recommendation.get(
            "strategic_rationale",
            "No strategic rationale available."
        )}

        </div>

        </div>
        """,
        unsafe_allow_html=True
    )


    # ========================================================
    # FINANCIAL + VALUATION
    # ========================================================

    financial_col, valuation_col = st.columns(2)

    with financial_col:

        st.markdown(
            """
            <div class="section-title">
                Financial Assessment
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div class="card">

            <div class="card-text">

            {recommendation.get(
                "financial_assessment",
                "No financial assessment available."
            )}

            </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    with valuation_col:

        st.markdown(
            """
            <div class="section-title">
                Valuation Assessment
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div class="card">

            <div class="card-text">

            {recommendation.get(
                "valuation_assessment",
                "No valuation assessment available."
            )}

            </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    # ========================================================
    # OPPORTUNITIES + RISKS
    # ========================================================

    opportunity_col, risk_col = st.columns(2)

    with opportunity_col:

        st.markdown(
            '<div class="section-title">🟢 Key Opportunities</div>',
            unsafe_allow_html=True
        )

        opportunities = recommendation.get(
            "key_opportunities",
            []
        )

        for opportunity in opportunities:

            st.success(
                opportunity,
                icon="✓"
            )


    with risk_col:

        st.markdown(
            '<div class="section-title">🔴 Key Risks</div>',
            unsafe_allow_html=True
        )

        risks = recommendation.get(
            "key_risks",
            []
        )

        for risk in risks:

            st.error(
                risk,
                icon="!"
            )


    # ========================================================
    # DETAILED DUE DILIGENCE
    # ========================================================

    st.markdown(
        '<div class="section-title">Detailed Due Diligence</div>',
        unsafe_allow_html=True
    )

    tab1, tab2, tab3 = st.tabs(
        [
            "⚖️ Regulatory",
            "⚙️ Integration",
            "📋 Conditions"
        ]
    )


    with tab1:

        regulatory = recommendation.get(
            "regulatory_concerns",
            []
        )

        if regulatory:

            for item in regulatory:
                st.warning(item)

        else:

            st.info(
                "No regulatory concerns were returned."
            )


    with tab2:

        integration = recommendation.get(
            "integration_concerns",
            []
        )

        if integration:

            for item in integration:
                st.info(item)

        else:

            st.info(
                "No integration concerns were returned."
            )


    with tab3:

        conditions = recommendation.get(
            "conditions_before_acquisition",
            []
        )

        if conditions:

            for i, condition in enumerate(
                conditions,
                start=1
            ):

                st.write(
                    f"**{i}.** {condition}"
                )

        else:

            st.info(
                "No acquisition conditions were returned."
            )


# ============================================================
# EVIDENCE
# ============================================================

st.divider()

st.markdown(
    '<div class="section-title">Evidence Intelligence</div>',
    unsafe_allow_html=True
)

evidence = result.get("evidence", []) or []


# ------------------------------------------------------------
# Normalize evidence
# ------------------------------------------------------------

normalized_evidence = []

for item in evidence:

    if hasattr(item, "model_dump"):
        item = item.model_dump()

    normalized_evidence.append(item)


# ------------------------------------------------------------
# Evidence summary
# ------------------------------------------------------------

evidence_col1, evidence_col2, evidence_col3 = st.columns(3)

with evidence_col1:

    st.metric(
        "Evidence Items",
        len(normalized_evidence)
    )

with evidence_col2:

    unique_sources = len(
        set(
            item.get(
                "source_name",
                "Unknown"
            )
            for item in normalized_evidence
        )
    )

    st.metric(
        "Sources",
        unique_sources
    )

with evidence_col3:

    high_credibility = sum(
        1
        for item in normalized_evidence
        if str(
            item.get(
                "credibility",
                ""
            )
        ).lower() == "high"
    )

    st.metric(
        "High Credibility",
        high_credibility
    )


# ------------------------------------------------------------
# Evidence filter
# ------------------------------------------------------------

if normalized_evidence:

    source_types = sorted(
        set(
            item.get(
                "source_type",
                "Unknown"
            )
            for item in normalized_evidence
        )
    )

    selected_type = st.selectbox(
        "Filter evidence by source type",
        ["All"] + source_types
    )


    filtered_evidence = normalized_evidence

    if selected_type != "All":

        filtered_evidence = [
            item
            for item in normalized_evidence
            if item.get(
                "source_type",
                "Unknown"
            ) == selected_type
        ]


    st.caption(
        f"Showing {len(filtered_evidence)} "
        f"of {len(normalized_evidence)} evidence items."
    )


    # --------------------------------------------------------
    # Evidence cards
    # --------------------------------------------------------

    for item in filtered_evidence:

        evidence_id = item.get(
            "evidence_id",
            "Unknown Evidence"
        )

        title = item.get(
            "title"
        ) or item.get(
            "source_name",
            "Unknown Source"
        )

        with st.expander(
            f"🔎 {evidence_id} — {title}"
        ):

            info_col1, info_col2, info_col3 = st.columns(3)

            with info_col1:

                st.write(
                    "**Source**"
                )

                st.write(
                    item.get(
                        "source_name",
                        "Unknown"
                    )
                )

            with info_col2:

                st.write(
                    "**Source Type**"
                )

                st.write(
                    item.get(
                        "source_type",
                        "Unknown"
                    )
                )

            with info_col3:

                st.write(
                    "**Credibility**"
                )

                st.write(
                    item.get(
                        "credibility",
                        "Unknown"
                    )
                )


            published_at = item.get(
                "published_at"
            )

            if published_at:

                st.write(
                    f"**Published:** {published_at}"
                )


            st.markdown(
                "### Extracted Evidence"
            )

            st.write(
                item.get(
                    "content",
                    "No evidence content available."
                )
            )


            st.markdown(
                "### Relevance"
            )

            st.write(
                item.get(
                    "relevance",
                    "No relevance explanation available."
                )
            )


            url = item.get("url")

            if url:

                st.markdown(
                    f"[🔗 View Original Source]({url})"
                )


else:

    st.info(
        "No evidence was returned by the workflow."
    )


# ============================================================
# DOWNLOAD REPORT
# ============================================================

st.divider()

st.markdown(
    '<div class="section-title">Export Analysis</div>',
    unsafe_allow_html=True
)


report_lines = []

report_lines.append(
    "M&A INTELLIGENCE — ACQUISITION ANALYSIS"
)

report_lines.append("=" * 60)

report_lines.append(
    f"Acquirer: {company_a}"
)

report_lines.append(
    f"Target: {company_b}"
)

report_lines.append(
    f"Question: {user_question}"
)

report_lines.append("")


if recommendation:

    report_lines.append(
        "FINAL RECOMMENDATION"
    )

    report_lines.append(
        recommendation.get(
            "recommendation",
            "N/A"
        )
    )

    report_lines.append(
        f"Confidence: {recommendation.get('confidence', 'N/A')}"
    )

    report_lines.append("")

    report_lines.append(
        "STRATEGIC RATIONALE"
    )

    report_lines.append(
        recommendation.get(
            "strategic_rationale",
            ""
        )
    )

    report_lines.append("")

    report_lines.append(
        "FINANCIAL ASSESSMENT"
    )

    report_lines.append(
        recommendation.get(
            "financial_assessment",
            ""
        )
    )

    report_lines.append("")

    report_lines.append(
        "VALUATION ASSESSMENT"
    )

    report_lines.append(
        recommendation.get(
            "valuation_assessment",
            ""
        )
    )

    report_lines.append("")

    report_lines.append(
        "KEY OPPORTUNITIES"
    )

    for item in recommendation.get(
        "key_opportunities",
        []
    ):

        report_lines.append(
            f"- {item}"
        )

    report_lines.append("")

    report_lines.append(
        "KEY RISKS"
    )

    for item in recommendation.get(
        "key_risks",
        []
    ):

        report_lines.append(
            f"- {item}"
        )

    report_lines.append("")

    report_lines.append(
        "REGULATORY CONCERNS"
    )

    for item in recommendation.get(
        "regulatory_concerns",
        []
    ):

        report_lines.append(
            f"- {item}"
        )

    report_lines.append("")

    report_lines.append(
        "INTEGRATION CONCERNS"
    )

    for item in recommendation.get(
        "integration_concerns",
        []
    ):

        report_lines.append(
            f"- {item}"
        )

    report_lines.append("")

    report_lines.append(
        "CONDITIONS BEFORE ACQUISITION"
    )

    for item in recommendation.get(
        "conditions_before_acquisition",
        []
    ):

        report_lines.append(
            f"- {item}"
        )


report = "\n".join(report_lines)


st.download_button(
    label="📥 Download Analysis Report",
    data=report,
    file_name="mna_acquisition_analysis.txt",
    mime="text/plain",
    use_container_width=True
)


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <br><br>

    <div style="
        text-align: center;
        color: #94a3b8;
        font-size: 0.85rem;
    ">

        M&A Intelligence • Autonomous Due-Diligence Platform

    </div>
    """,
    unsafe_allow_html=True
)