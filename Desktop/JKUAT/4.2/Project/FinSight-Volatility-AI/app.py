import streamlit as st

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="FinSight AI",
    page_icon="📈",
    layout="wide"
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

/* Sidebar text */

section[data-testid="stSidebar"] *{
    color:white !important;
}

/* Navigation area */

[data-testid="stSidebarNav"]{
    padding-top:10px;
}

/* Navigation buttons */

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

/* Hover effect */

[data-testid="stSidebarNav"] a:hover{
    background:#1E3A5F;
    border-color:#3B82F6;
    transform:translateX(3px);
}

/* Active page */

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

/* Navigation list spacing */

[data-testid="stSidebarNav"] ul{
    gap:8px;
}

/* =====================================================
   MAIN PAGE
===================================================== */

.main{
    background:#F8FAFC;
}

/* =====================================================
   METRIC CARDS
===================================================== */

div[data-testid="metric-container"]{
    background:white;
    border-radius:12px;
    border:1px solid #E5E7EB;
    padding:15px;
    box-shadow:0px 2px 8px rgba(
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
Machine Learning-based stock volatility forecasting,
portfolio risk management and executive decision support
for companies listed on the Nairobi Securities Exchange (NSE).
""")

st.divider()

# =====================================================
# PROJECT STATISTICS
# =====================================================

st.subheader("Project Statistics")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        "Stocks Analyzed",
        "68"
    )

with c2:
    st.metric(
        "Records Processed",
        "32,000+"
    )

with c3:
    st.metric(
        "Model Accuracy (R²)",
        "98.64%"
    )

with c4:
    st.metric(
        "Risk Engine",
        "Random Forest"
    )

st.divider()

# =====================================================
# RESEARCH PROJECT
# =====================================================

st.subheader("Research Project")

st.markdown("""
**Machine Learning-Based Stock Volatility Forecasting and
Executive Risk Intelligence Platform for Companies Listed
on the Nairobi Securities Exchange (NSE).**
""")

st.subheader("Author")

st.write("Joseph Abuya Abich")

st.divider()

# =====================================================
# EXECUTIVE OVERVIEW
# =====================================================

st.subheader("Executive Overview")

st.write("""
FinSight AI is a Machine Learning-powered financial intelligence
platform designed to forecast stock volatility and support
investment decision-making.
""")

st.write("""
The platform combines Random Forest forecasting, risk scoring,
executive dashboards, portfolio intelligence, board reporting,
and AI-driven investment recommendations.
""")

st.divider()

# =====================================================
# PLATFORM MODULES
# =====================================================

st.subheader("Platform Modules")

st.success("✅ Market Explorer")
st.success("✅ Volatility Forecasting")
st.success("✅ Model Performance")
st.success("✅ Research Findings")
st.success("✅ Executive Dashboard")
st.success("✅ AI Advisory Center")
st.success("✅ Board Pack")
st.success("✅ Portfolio Risk Simulator")

st.divider()

# =====================================================
# FOOTER
# =====================================================

st.info("""
Built using Python, Streamlit, Plotly,
Machine Learning and Financial Analytics.
""")