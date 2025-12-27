from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import json

load_dotenv()
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

ingestion_Prompt = PromptTemplate(
    input_variables=["report"],
    template="""

Role: You are a security risk analysis agent.

Rules:
- Do NOT analyze or recommend.
- If a field is missing, use null.
- Respond in ONLY valid JSON.

Output format:

{{
    "component": string or null,
    "issue":string or null,
    "severity": "LOW | MEDIUM | HIGH | UNKNOWN",
    "cve_id": string or null,
    "summary": string
}}

Security Report:
{report}
"""
)

#LangGraph Node: Ingestion Agent

def ingestion_agent(state: dict) -> dict:

    raw_report = state["raw_report"]
    prompt = ingestion_Prompt.format(report=raw_report)
    response = llm.invoke(prompt)

    #Incase of any error occurance during parsing
    try:
        parsed_report = json.loads(response.content)
    except json.JSONDecodeError:
        parsed_report = {
            "component": None,
            "issue": None,
            "severity": "UNKNOWN",
            "cve_id": None,
            "summary": "Failed to parse LLM response."
        }

    state["parsed_report"] = parsed_report
    return state

