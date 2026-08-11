from google import genai


def ask_financial_ai(financial_data, question):
    try:
        client = genai.Client()

        prompt = f"""
You are FinSight, an AI Financial Analyst.

The user has uploaded the following financial statement data:

{financial_data}

Answer the user's question using the financial data above.

User question:
{question}

Rules:
- Give a clear and professional answer.
- Use ₹ for monetary values where appropriate.
- Do not invent financial data.
- If the requested information is not available, clearly say so.
- Explain financial terms in simple language.
"""

        response = client.models.generate_content(
           model="models/gemini-3.5-flash",
            contents=prompt,
        )

        return response.text

    except Exception as e:
        return f"❌ AI Error: {str(e)}"