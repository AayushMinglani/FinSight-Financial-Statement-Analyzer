import streamlit as st
import pandas as pd
from io import BytesIO

from charts import show_all_charts
from dashboard import show_dashboard
from pdf_report import generate_pdf
from pdf_parser import extract_financial_data_from_pdf
from analyzer import calculate_health_score, get_health_status, generate_recommendations, detect_financial_risks
from ai_analyst import ask_financial_ai
from styles import load_css


APP_NAME = "FinSight"
APP_TAGLINE = "AI-Powered Financial Statement Analyzer"
APP_VERSION = "Version 2.0"
DEVELOPER = "Aayush Minglani"


st.set_page_config(
    page_title=APP_NAME,
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

load_css()


# ---------------- CUSTOM UI ---------------- #

st.markdown(
    """
<style>

.stApp{
background:linear-gradient(135deg,#0f172a,#1e3a8a,#2563eb);
background-attachment:fixed;
}

section[data-testid="stSidebar"]{
background:#0b1220;
}

section[data-testid="stSidebar"] *{
color:white;
}

.main-title{
font-size:55px;
font-weight:800;
color:white;
text-align:center;
margin-bottom:0px;
}

.sub-title{
font-size:22px;
text-align:center;
color:#dbeafe;
margin-bottom:40px;
}

.glass{
background:rgba(255,255,255,0.08);
padding:25px;
border-radius:20px;
backdrop-filter:blur(14px);
border:1px solid rgba(255,255,255,0.15);
margin-bottom:25px;
color:white;
}

div[data-testid="metric-container"]{
background:rgba(255,255,255,0.10);
border:1px solid rgba(255,255,255,0.15);
padding:20px;
border-radius:18px;
backdrop-filter:blur(12px);
}

div[data-testid="metric-container"] label{
color:white;
}

div[data-testid="metric-container"] div{
color:white;
}

.stButton>button{
background:#2563eb;
color:white;
border:none;
border-radius:10px;
font-weight:bold;
}

.stButton>button:hover{
background:#1d4ed8;
}

hr{
border:1px solid rgba(255,255,255,0.15);
}

</style>
""",
    unsafe_allow_html=True,
)


# ---------------- SESSION ---------------- #

if "financial_data" not in st.session_state:
    st.session_state.financial_data = {}

if "uploaded_df" not in st.session_state:
    st.session_state.uploaded_df = None


# ---------------- SIDEBAR ---------------- #

st.sidebar.image(
    "https://img.icons8.com/fluency/96/combo-chart.png",
    width=80,
)

st.sidebar.title(APP_NAME)
st.sidebar.caption(APP_TAGLINE)

page = st.sidebar.radio(
    "Navigation",
    ["🏠 Home", "📂 Analyze Statement", "📈 Dashboard", "📄 Reports", "ℹ About"],
)


# ---------------- HOME ---------------- #

if page == "🏠 Home":

    st.markdown(
        '<p class="main-title">📊 FinSight</p>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<p class="sub-title">AI Powered Financial Statement Analyzer</p>',
        unsafe_allow_html=True,
    )

    st.markdown(
        """
<div class="glass">

### 🚀 Features

✅ Upload Excel / CSV Statements

✅ Automatic Financial Summary

✅ Ratio Analysis

✅ Interactive Charts

✅ Financial Health Score

✅ AI Recommendations

✅ Professional Dashboard

✅ Business Reports

</div>
""",
        unsafe_allow_html=True,
    )

    st.info(
        "👈 Start by opening **Analyze Statement** from the sidebar."
    )


# ---------------- ANALYZE STATEMENT ---------------- #

if page == "📂 Analyze Statement":

    st.title("📂 Analyze Financial Statement")

    st.markdown(
        """
<div class="glass">

Upload your company's Excel, CSV or PDF Financial Statement.

Supported formats:

• Excel (.xlsx)

• Excel (.xls)

• CSV (.csv)

• PDF (.pdf)

</div>
""",
        unsafe_allow_html=True,
    )

    uploaded_file = st.file_uploader(
        "Choose Financial Statement",
        type=["xlsx", "xls", "csv", "pdf"],
    )

    if uploaded_file is not None:

        financial_data = {}

        if uploaded_file.name.endswith(".csv"):

            df = pd.read_csv(uploaded_file)

            st.session_state.uploaded_df = df

            st.markdown("## 📑 Data Preview")

            st.dataframe(
                df,
                use_container_width=True,
            )

            for _, row in df.iterrows():

                item = str(row.iloc[0]).lower()
                value = row.iloc[1]

                if "revenue" in item or "sales" in item:
                    financial_data["Revenue"] = value

                elif "gross profit" in item:
                    financial_data["Gross Profit"] = value

                elif "operating profit" in item:
                    financial_data["Operating Profit"] = value

                elif "net profit" in item:
                    financial_data["Net Profit"] = value

        elif uploaded_file.name.endswith((".xlsx", ".xls")):

            df = pd.read_excel(uploaded_file)

            st.session_state.uploaded_df = df

            st.markdown("## 📑 Data Preview")

            st.dataframe(
                df,
                use_container_width=True,
            )

            for _, row in df.iterrows():

                item = str(row.iloc[0]).lower()
                value = row.iloc[1]

                if "revenue" in item or "sales" in item:
                    financial_data["Revenue"] = value

                elif "gross profit" in item:
                    financial_data["Gross Profit"] = value

                elif "operating profit" in item:
                    financial_data["Operating Profit"] = value

                elif "net profit" in item:
                    financial_data["Net Profit"] = value

        elif uploaded_file.name.endswith(".pdf"):

            financial_data = extract_financial_data_from_pdf(
                uploaded_file
            )

            st.success("✅ PDF Uploaded Successfully")

            st.json(financial_data)

        st.session_state.financial_data = financial_data

        st.success("✅ Financial Statement Uploaded Successfully")

        if financial_data:

            st.markdown("---")

            st.subheader("📊 Financial Summary")

            col1, col2, col3, col4 = st.columns(4)

            if "Revenue" in financial_data:
                col1.metric(
                    "Revenue",
                    f"₹ {financial_data['Revenue']:,.0f}",
                )

            if "Gross Profit" in financial_data:
                col2.metric(
                    "Gross Profit",
                    f"₹ {financial_data['Gross Profit']:,.0f}",
                )

            if "Operating Profit" in financial_data:
                col3.metric(
                    "Operating Profit",
                    f"₹ {financial_data['Operating Profit']:,.0f}",
                )

            if "Net Profit" in financial_data:
                col4.metric(
                    "Net Profit",
                    f"₹ {financial_data['Net Profit']:,.0f}",
                )

            st.markdown("---")

            st.markdown("---")

            st.subheader("📈 Financial Ratios")

            if "Revenue" in financial_data and financial_data["Revenue"] != 0:

                ratio1, ratio2, ratio3 = st.columns(3)

                if "Gross Profit" in financial_data:

                    gross_margin = (
                        financial_data["Gross Profit"]
                        / financial_data["Revenue"]
                    ) * 100

                    ratio1.metric(
                        "Gross Margin",
                        f"{gross_margin:.2f}%"
                    )

                if "Operating Profit" in financial_data:

                    operating_margin = (
                        financial_data["Operating Profit"]
                        / financial_data["Revenue"]
                    ) * 100

                    ratio2.metric(
                        "Operating Margin",
                        f"{operating_margin:.2f}%"
                    )

                if "Net Profit" in financial_data:

                    net_margin = (
                        financial_data["Net Profit"]
                        / financial_data["Revenue"]
                    ) * 100

                    ratio3.metric(
                        "Net Margin",
                        f"{net_margin:.2f}%"
                    )

            if "Assets" in financial_data:

                st.markdown("### 🏦 Balance Sheet Ratios")

                balance_ratio1, balance_ratio2, balance_ratio3 = st.columns(3)

                if "Liabilities" in financial_data:

                    debt_to_asset = (
                        financial_data["Liabilities"]
                        / financial_data["Assets"]
                    ) * 100

                    balance_ratio1.metric(
                        "Debt-to-Asset",
                        f"{debt_to_asset:.2f}%"
                    )

                if "Equity" in financial_data:

                    equity_ratio = (
                        financial_data["Equity"]
                        / financial_data["Assets"]
                    ) * 100

                    balance_ratio2.metric(
                        "Equity Ratio",
                        f"{equity_ratio:.2f}%"
                    )

                if "Liabilities" in financial_data and financial_data["Equity"] != 0:

                    debt_to_equity = (
                        financial_data["Liabilities"]
                        / financial_data["Equity"]
                    )

                    balance_ratio3.metric(
                        "Debt-to-Equity",
                        f"{debt_to_equity:.2f}x"
                    )

            show_all_charts(financial_data)

            st.markdown("---")

            st.subheader("🧠 Financial Health Analysis")

            score = calculate_health_score(financial_data)

            status = get_health_status(score)

            recommendations = generate_recommendations(
                financial_data
            )
            risks = detect_financial_risks(financial_data)

            if risks:

                st.markdown("### 🚨 Financial Risks")

                for risk in risks:

                    st.warning(risk)

            else:

                st.success(
                    "✅ No major financial risks detected."
                )

            score_col, status_col = st.columns(2)

            with score_col:

                st.metric(
                    "Financial Health Score",
                    f"{score}/100",
                )

            with status_col:

                st.metric(
                    "Overall Status",
                    status,
                )

            pdf = generate_pdf(
                financial_data,
                score,
                status,
                recommendations,
            )

            st.download_button(
                label="📄 Download Financial Report",
                data=pdf,
                file_name="FinSight_Report.pdf",
                mime="application/pdf",
            )

            st.markdown("### 💡 AI Recommendations")

            for recommendation in recommendations:

                st.success(recommendation)

            st.markdown("---")

            st.subheader("🤖 AI Financial Analyst")

            st.write(
                "Ask questions about the uploaded financial statement."
            )

            question = st.chat_input(
                "Ask something about the company's finances..."
            )

            if question:

                with st.chat_message("user"):

                    st.write(question)

                with st.chat_message("assistant"):

                    answer = ask_financial_ai(
                        financial_data,
                        question
                    )

                    st.write(answer)

            st.markdown("---")

            with st.expander(
                "📄 File Information",
                expanded=False,
            ):

                st.write(
                    f"**File Name:** {uploaded_file.name}"
                )

                st.write(
                    f"**File Type:** {uploaded_file.type}"
                )

                st.write(
                    f"**File Size:** {round(uploaded_file.size / 1024, 2)} KB"
                )


# ---------------- DASHBOARD ---------------- #
if page == "📈 Dashboard":

    if st.session_state.financial_data:

        show_dashboard(
            st.session_state.financial_data
        )

    else:

        st.title("📈 Business Dashboard")

        st.warning(
            "Please upload a financial statement first."
        )


# ---------------- REPORTS ---------------- #

elif page == "📄 Reports":

    st.title("📄 Financial Reports")

    if st.session_state.financial_data:

        data = st.session_state.financial_data

        report = pd.DataFrame(
            {
                "Metric": list(data.keys()),
                "Value": list(data.values()),
            }
        )

        st.dataframe(
            report,
            use_container_width=True,
        )

        score = calculate_health_score(data)

        status = get_health_status(score)

        recommendations = generate_recommendations(data)

        pdf = generate_pdf(
            data,
            score,
            status,
            recommendations,
        )

        st.download_button(
            label="📄 Download PDF Report",
            data=pdf,
            file_name="FinSight_Report.pdf",
            mime="application/pdf",
        )

    else:

        st.warning(
            "Upload a financial statement first."
        )


# ---------------- ABOUT ---------------- #

elif page == "ℹ About":

    st.title("ℹ About FinSight")

    st.markdown(
        """
<div class="glass">

## 📊 FinSight

FinSight is an AI Powered Financial Statement Analyzer.

### Features

- 📂 Excel & CSV / PDF Upload
- 📈 Interactive Charts
- 📊 Financial Ratios
- 🧠 Financial Health Score
- 💡 Smart Recommendations
- 📄 Download Reports
- 📉 Business Dashboard

---

### 👨‍💻 Developer

**Aayush Minglani**

Version 2.0

</div>
""",
        unsafe_allow_html=True,
    )