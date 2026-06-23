import streamlit as st

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="FinSight AI",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================================
# EXECUTIVE STYLING
# =====================================================

st.markdown("""
<style>

/* =====================================================
   EXECUTIVE SIDEBAR
===================================================== */

section[data-testid="stSidebar"]{
    background:#0B132B;
}

section[data-testid="stSidebar"] *{
    color:white !important;
}

[data-testid="stSidebarNav"]{
    padding-top:10px;
}

[data-testid="stSidebarNav"] a{
    background:#16213E;
    border:1px solid #243B55;
    border-radius:12px;
    padding:12px 15px;
    margin-bottom:8px;
    text-decoration:none;
    font-weight:600;
    transition:all .3s ease;
    display:block;
}

[data-testid="stSidebarNav"] a:hover{
    background:#1E3A5F;
    border-color:#3B82F6;
    transform:translateX(3px);
}

[data-testid="stSidebarNav"] a[aria-current="page"]{
    background:linear-gradient(
        90deg,
        #2563EB,
        #3B82F6
    ) !important;

    color:white !important;
    border:none !important;

    box-shadow:
        0px 4px 12px rgba(
            59,
            130,
            246,
            0.4
        );

    font-weight:700 !important;
}

[data-testid="stSidebarNav"] ul{
    gap:8px;
}

/* =====================================================
   MAIN PAGE
===================================================== */

.main{
    background:#F8FAFC;
}

.main .block-container{
    max-width:95%;
    padding-top:2rem;
    padding-left:2rem;
    padding-right:2rem;
}

/* =====================================================
   METRIC CARDS
===================================================== */

div[data-testid="metric-container"]{
    background:white;
    border-radius:12px;
    border:1px solid #E5E7EB;
    padding:15px;

    box-shadow:
    0px 2px 8px rgba(
        0,
        0,
        0,
        0.05
    );
}

/* =====================================================
   HEADERS
===================================================== */

h1{
    color:#0F172A;
}

h2{
    color:#1E293B;
}

h3{
    color:#1E293B;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# SIDEBAR BRANDING
# =====================================================

st.sidebar.markdown("""
# 📈 FinSight AI

### Executive Market Risk
### Intelligence Platform

---
""")

# =====================================================
# HOME PAGE
# =====================================================

st.title("📈 FinSight AI")

st.header(
    "Executive Market Risk Intelligence Platform"
)

st.markdown("""
Machine Learning-powered volatility forecasting,
market risk intelligence and executive decision
support for securities listed on the Nairobi
Securities Exchange (NSE).
""")

st.divider()

# =====================================================
# PLATFORM STATISTICS
# =====================================================

st.subheader("Platform Statistics")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        "Securities Analyzed",
        "68"
    )

with c2:
    st.metric(
        "Records Processed",
        "32,000+"
    )

with c3:
    st.metric(
        "Model R² Score",
        "0.9864"
    )

with c4:
    st.metric(
        "Forecasting Engine",
        "Random Forest"
    )

st.divider()

# =====================================================
# PLATFORM OBJECTIVE
# =====================================================

st.subheader("Platform Objective")

st.markdown("""
FinSight AI provides volatility forecasting,
market risk intelligence, portfolio analytics
and executive reporting capabilities for
Nairobi Securities Exchange listed securities.
""")

st.write("""
The platform is designed to support portfolio
managers, financial analysts, executives,
boards and risk management teams through
data-driven market risk assessment.
""")

st.divider()

# =====================================================
# EXECUTIVE OVERVIEW
# =====================================================

st.subheader("Executive Overview")

st.write("""
FinSight AI combines machine learning
forecasting, volatility risk scoring,
executive dashboards, portfolio analytics,
board reporting and risk intelligence
capabilities into a single platform.
""")

st.write("""
The platform enables users to identify
volatility risk patterns, monitor market
conditions and support investment governance
through objective, data-driven insights.
""")

st.divider()

# =====================================================
# PLATFORM MODULES
# =====================================================

st.subheader("Platform Modules")

st.success("✅ Market Explorer")
st.success("✅ Volatility Forecasting")
st.success("✅ Predictive Model Performance")
st.success("✅ Market Risk Insights")
st.success("✅ Executive Dashboard")
st.success("✅ Risk Intelligence Center")
st.success("✅ Board Pack")
st.success("✅ Portfolio Risk Simulator")

st.divider()

# =====================================================
# KEY CAPABILITIES
# =====================================================

st.subheader("Key Capabilities")

st.markdown("""
- Forecast future volatility using Machine Learning
- Classify securities by volatility risk level
- Monitor market risk concentration
- Compare securities using volatility rankings
- Generate executive and board-level risk reports
- Support portfolio monitoring and risk governance
""")

st.divider()

# =====================================================
# FOOTER
# =====================================================

st.info("""
Built using Python, Streamlit, Plotly,
Machine Learning and Financial Analytics.
""")