import streamlit as st
import plotly.express as px
import pandas as pd


def show_dashboard(financial_data):

    st.title("📈 Business Intelligence Dashboard")

    if not financial_data:

        st.warning(
            "Please upload a financial statement first."
        )

        return

    revenue = financial_data.get("Revenue", 0)
    gross = financial_data.get("Gross Profit", 0)
    operating = financial_data.get("Operating Profit", 0)
    net = financial_data.get("Net Profit", 0)

    st.subheader("📊 Key Financial Metrics")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Revenue",
        f"₹ {revenue:,.0f}"
    )

    col2.metric(
        "Gross Profit",
        f"₹ {gross:,.0f}"
    )

    col3.metric(
        "Operating Profit",
        f"₹ {operating:,.0f}"
    )

    col4.metric(
        "Net Profit",
        f"₹ {net:,.0f}"
    )

    st.markdown("---")

    if revenue != 0:

        gross_margin = (gross / revenue) * 100
        operating_margin = (operating / revenue) * 100
        net_margin = (net / revenue) * 100

        st.subheader("📈 Profitability Ratios")

        r1, r2, r3 = st.columns(3)

        r1.metric(
            "Gross Margin",
            f"{gross_margin:.2f}%"
        )

        r2.metric(
            "Operating Margin",
            f"{operating_margin:.2f}%"
        )

        r3.metric(
            "Net Margin",
            f"{net_margin:.2f}%"
        )

    st.markdown("---")

    chart_df = pd.DataFrame(

        {
            "Metric": [
                "Revenue",
                "Gross Profit",
                "Operating Profit",
                "Net Profit"
            ],

            "Amount": [
                revenue,
                gross,
                operating,
                net
            ]
        }

    )

    fig = px.bar(

        chart_df,

        x="Metric",

        y="Amount",

        color="Metric",

        title="Business Performance Overview"

    )

    fig.update_layout(

        template="plotly_dark",

        paper_bgcolor="rgba(0,0,0,0)",

        plot_bgcolor="rgba(0,0,0,0)",

        height=500

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )   
    st.markdown("---")

    st.subheader("📌 Business Insights")

    if net > 0:

        st.success(
            "🟢 Your business is currently profitable."
        )

    elif net == 0:

        st.warning(
            "🟡 Your business is currently at break-even."
        )

    else:

        st.error(
            "🔴 Your business is currently making a loss."
        )

    st.markdown("---")

    st.subheader("💰 Revenue Distribution")

    pie = px.pie(

        chart_df,

        names="Metric",

        values="Amount",

        hole=0.55,

        color="Metric",

        color_discrete_sequence=[
            "#3b82f6",
            "#22c55e",
            "#f59e0b",
            "#ef4444"
        ]

    )

    pie.update_layout(

        template="plotly_dark",

        paper_bgcolor="rgba(0,0,0,0)",

        plot_bgcolor="rgba(0,0,0,0)",

        height=500

    )

    st.plotly_chart(
        pie,
        use_container_width=True
    )

    st.markdown("---")

    st.caption("© 2026 FinSight • Developed by Aayush Minglani")
    