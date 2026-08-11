# FinSight – AI Financial Statement Analyzer

FinSight is an AI-powered financial statement analysis application that helps users upload financial documents, extract financial information, analyze key financial metrics, visualize financial performance, and ask questions about their financial statements using AI.

## 🚀 Features

- 📄 Upload financial statements in PDF, CSV, and Excel formats
- 🔍 Extract and process financial data from uploaded documents
- 📊 Calculate important financial ratios and margins
- 📈 Visualize financial performance using charts and dashboards
- 🧮 Analyze profitability, leverage, and financial health
- ⚠️ Identify potential financial risks
- 💡 Generate financial recommendations based on the available data
- 🤖 Ask questions about uploaded financial statements using Gemini AI
- 📝 Generate downloadable financial analysis reports
- 📑 Generate PDF reports containing analysis and insights
- 🛡️ Includes safeguards when sufficient financial data is not available

## 📊 Financial Analysis

FinSight can analyze financial indicators such as:

- Gross Profit Margin
- Operating Margin
- Net Profit Margin
- Debt-to-Asset Ratio
- Debt-to-Equity Ratio
- Equity Position
- Overall Financial Health
- Potential Financial Risks
- Financial Recommendations

## 🤖 AI Financial Analyst

The application includes an AI Financial Analyst powered by Google's Gemini API.

Users can ask questions about an uploaded financial statement, such as:

- What is the gross profit?
- What is the company's net profit margin?
- Is the company highly leveraged?
- What are the major financial risks?
- How is the company's profitability?
- What financial areas require attention?

The AI is designed to use the available financial statement data and avoid making unsupported conclusions when required information is unavailable.

## 🏗️ Project Structure

```text
FinSight-Financial-Statement-Analyzer/
│
├── app.py
├── ai_analyst.py
├── analyzer.py
├── charts.py
├── dashboard.py
├── pdf_parser.py
├── pdf_report.py
├── styles.py
├── test.py
├── .gitignore
└── README.md