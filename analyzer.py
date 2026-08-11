def calculate_health_score(financial_data):

    revenue = financial_data.get("Revenue", 0)
    gross = financial_data.get("Gross Profit", 0)
    operating = financial_data.get("Operating Profit", 0)
    net = financial_data.get("Net Profit", 0)

    score = 0

    if revenue <= 0:
        return 0

    gross_margin = (gross / revenue) * 100
    operating_margin = (operating / revenue) * 100
    net_margin = (net / revenue) * 100

    if gross_margin >= 50:
        score += 30
    elif gross_margin >= 35:
        score += 25
    elif gross_margin >= 20:
        score += 15
    else:
        score += 5

    if operating_margin >= 25:
        score += 30
    elif operating_margin >= 15:
        score += 25
    elif operating_margin >= 8:
        score += 15
    else:
        score += 5

    if net_margin >= 20:
        score += 40
    elif net_margin >= 15:
        score += 35
    elif net_margin >= 10:
        score += 25
    elif net_margin >= 5:
        score += 15
    else:
        score += 5

    return min(score, 100)
def get_health_status(score):

    if score >= 90:
        return "🟢 Excellent"

    elif score >= 75:
        return "🟢 Very Good"

    elif score >= 60:
        return "🟡 Good"

    elif score >= 45:
        return "🟠 Average"

    elif score >= 25:
        return "🔴 Weak"

    return "⚫ Critical"


def get_performance_grade(score):

    if score >= 90:
        return "A+"

    elif score >= 80:
        return "A"

    elif score >= 70:
        return "B"

    elif score >= 60:
        return "C"

    elif score >= 50:
        return "D"

    return "F"


def get_risk_level(score):

    if score >= 85:
        return "🟢 Low Risk"

    elif score >= 65:
        return "🟡 Moderate Risk"

    elif score >= 45:
        return "🟠 High Risk"

    return "🔴 Very High Risk"
def generate_recommendations(financial_data):

    recommendations = []

    revenue = financial_data.get("Revenue", 0)
    gross = financial_data.get("Gross Profit", 0)
    operating = financial_data.get("Operating Profit", 0)
    net = financial_data.get("Net Profit", 0)

    if revenue <= 0:
        recommendations.append(
            "Upload a valid financial statement."
        )
        return recommendations

    gross_margin = (gross / revenue) * 100
    operating_margin = (operating / revenue) * 100
    net_margin = (net / revenue) * 100

    if gross_margin < 25:
        recommendations.append(
            "📉 Reduce Cost of Goods Sold (COGS) to improve Gross Profit Margin."
        )

    if operating_margin < 15:
        recommendations.append(
            "💼 Reduce operating expenses and improve operational efficiency."
        )

    if net_margin < 10:
        recommendations.append(
            "📈 Increase revenue or reduce unnecessary costs to improve Net Profit."
        )

    if net_margin >= 20:
        recommendations.append(
            "🏆 Excellent profitability. Continue maintaining strong financial performance."
        )

    if revenue > 10000000:
        recommendations.append(
            "🚀 Business scale looks strong. Consider expansion opportunities."
        )

    if len(recommendations) == 0:
        recommendations.append(
            "✅ Financial performance looks healthy with no major concerns."
        )

    return recommendations

def detect_financial_risks(financial_data):

    risks = []

    if "Revenue" in financial_data and "Net Profit" in financial_data:

        if financial_data["Revenue"] > 0:

            net_margin = (
                financial_data["Net Profit"]
                / financial_data["Revenue"]
            ) * 100

            if net_margin < 5:
                risks.append(
                    f"⚠️ Low net profit margin: {net_margin:.2f}%"
                )

            if net_margin < 0:
                risks.append(
                    "🚨 Company is reporting a net loss."
                )

    if "Assets" in financial_data and "Liabilities" in financial_data:

        if financial_data["Assets"] > 0:

            debt_to_asset = (
                financial_data["Liabilities"]
                / financial_data["Assets"]
            ) * 100

            if debt_to_asset > 70:
                risks.append(
                    f"🚨 High debt-to-asset ratio: {debt_to_asset:.2f}%"
                )

            elif debt_to_asset > 50:
                risks.append(
                    f"⚠️ Elevated debt-to-asset ratio: {debt_to_asset:.2f}%"
                )

    if "Liabilities" in financial_data and "Equity" in financial_data:

        if financial_data["Equity"] > 0:

            debt_to_equity = (
                financial_data["Liabilities"]
                / financial_data["Equity"]
            )

            if debt_to_equity > 2:
                risks.append(
                    f"🚨 High debt-to-equity ratio: {debt_to_equity:.2f}x"
                )

            elif debt_to_equity > 1:
                risks.append(
                    f"⚠️ Elevated debt-to-equity ratio: {debt_to_equity:.2f}x"
                )

    if "Gross Profit" in financial_data and "Revenue" in financial_data:

        if financial_data["Revenue"] > 0:

            gross_margin = (
                financial_data["Gross Profit"]
                / financial_data["Revenue"]
            ) * 100

            if gross_margin < 20:
                risks.append(
                    f"⚠️ Low gross margin: {gross_margin:.2f}%"
                )

    return risks