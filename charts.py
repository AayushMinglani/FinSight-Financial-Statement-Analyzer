import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


def prepare_chart_data(financial_data):

    chart_data = []

    metrics = [
        "Revenue",
        "Gross Profit",
        "Operating Profit",
        "Net Profit"
    ]

    for metric in metrics:

        if metric in financial_data:

            chart_data.append(

                {
                    "Category": metric,
                    "Amount": financial_data[metric]
                }

            )

    return pd.DataFrame(chart_data)


def show_bar_chart(financial_data):

    chart_df = prepare_chart_data(financial_data)

    if chart_df.empty:
        return

    fig = px.bar(

        chart_df,

        x="Category",

        y="Amount",

        text="Amount",

        color="Category",

        title="Financial Performance Overview",

        color_discrete_sequence=[
            "#38bdf8",
            "#22c55e",
            "#f59e0b",
            "#ef4444"
        ]

    )   
    fig.update_traces(

        texttemplate="₹ %{y:,.0f}",

        textposition="outside",

        marker_line_color="white",

        marker_line_width=2

    )

    fig.update_layout(

        template="plotly_dark",

        paper_bgcolor="rgba(0,0,0,0)",

        plot_bgcolor="rgba(0,0,0,0)",

        font=dict(
            color="white",
            size=14
        ),

        title_font_size=24,

        height=550,

        showlegend=False

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


def show_pie_chart(financial_data):

    chart_df = prepare_chart_data(financial_data)

    if chart_df.empty:
        return

    fig = px.pie(

        chart_df,

        names="Category",

        values="Amount",

        hole=0.55,

        color="Category",

        title="Financial Distribution",

        color_discrete_sequence=[
            "#38bdf8",
            "#22c55e",
            "#f59e0b",
            "#ef4444"
        ]

    )    
    fig.update_traces(

        textinfo="percent+label",

        pull=[0.03, 0.03, 0.03, 0.03],

        marker=dict(
            line=dict(
                color="white",
                width=2
            )
        )

    )

    fig.update_layout(

        template="plotly_dark",

        paper_bgcolor="rgba(0,0,0,0)",

        plot_bgcolor="rgba(0,0,0,0)",

        font=dict(
            color="white",
            size=14
        ),

        title_font_size=24,

        height=550

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


def show_line_chart(financial_data):

    chart_df = prepare_chart_data(financial_data)

    if chart_df.empty:
        return

    fig = px.line(

        chart_df,

        x="Category",

        y="Amount",

        markers=True,

        title="Financial Trend",

        color_discrete_sequence=["#38bdf8"]

    )  
    fig.update_traces(

        line=dict(
            width=5
        ),

        marker=dict(
            size=12
        )

    )

    fig.update_layout(

        template="plotly_dark",

        paper_bgcolor="rgba(0,0,0,0)",

        plot_bgcolor="rgba(0,0,0,0)",

        font=dict(
            color="white",
            size=14
        ),

        title_font_size=24,

        height=550,

        xaxis_title="Financial Metrics",

        yaxis_title="Amount (₹)"

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


def show_all_charts(financial_data):

    st.markdown("---")

    st.subheader("📊 Interactive Financial Charts")

    tab1, tab2, tab3 = st.tabs(

        [
            "📈 Bar Chart",
            "🥧 Pie Chart",
            "📉 Line Chart"
        ]

    )

    with tab1:
        show_bar_chart(financial_data)

    with tab2:
        show_pie_chart(financial_data)

    with tab3:
        show_line_chart(financial_data)