import pdfplumber
import re


def extract_financial_data_from_pdf(uploaded_file):

    financial_data = {}

    with pdfplumber.open(uploaded_file) as pdf:

        full_text = ""

        for page in pdf.pages:

            text = page.extract_text()

            if text:
                full_text += text + "\n"

    # Normalize text
    full_text = re.sub(r"\s+", " ", full_text)

    patterns = {

        "Revenue": r"(?:Revenue|Sales|Turnover|Revenue from Operations|Total Income)"
        r"[^0-9₹$£€-]*"
        r"(-?\(?[\d,]+(?:\.\d+)?\)?)",

        "Gross Profit": r"(?:Gross Profit|Gross Income)"
        r"[^0-9₹$£€-]*"
        r"(-?\(?[\d,]+(?:\.\d+)?\)?)",

        "Operating Profit": r"(?:Operating Profit|Operating Income|EBIT)"
        r"[^0-9₹$£€-]*"
        r"(-?\(?[\d,]+(?:\.\d+)?\)?)",

        "Net Profit": r"(?:Net Profit|Net Income|Profit After Tax|PAT|Profit for the Year)"
        r"[^0-9₹$£€-]*"
        r"(-?\(?[\d,]+(?:\.\d+)?\)?)",

        "Assets": r"(?:Total Assets)"
        r"[^0-9₹$£€-]*"
        r"(-?\(?[\d,]+(?:\.\d+)?\)?)",

        "Liabilities": r"(?:Total Liabilities)"
        r"[^0-9₹$£€-]*"
        r"(-?\(?[\d,]+(?:\.\d+)?\)?)",

        "Equity": r"(?:Total Equity|Shareholders.? Equity|Stockholders.? Equity)"
        r"[^0-9₹$£€-]*"
        r"(-?\(?[\d,]+(?:\.\d+)?\)?)"
    }

    for key, pattern in patterns.items():

        match = re.search(
            pattern,
            full_text,
            re.IGNORECASE
        )

        if match:

            value = match.group(1)

            # Remove currency symbols and commas
            value = value.replace(",", "")
            value = re.sub(r"[₹$£€]", "", value)

            # Handle values written like (1,250,000)
            if value.startswith("(") and value.endswith(")"):

                value = "-" + value[1:-1]

            try:

                financial_data[key] = float(value)

            except ValueError:

                financial_data[key] = 0

    return financial_data