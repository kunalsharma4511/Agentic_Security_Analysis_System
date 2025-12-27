from dotenv import load_dotenv
load_dotenv()

import json
import os
from huggingface_hub import InferenceClient

client = InferenceClient(
    token=os.getenv("HF_TOKEN")
)

MODEL_NAME = "mistralai/Mistral-7B-Instruct-v0.2"

SYSTEM_PROMPT = """
You are a security risk analysis agent.

You must return ONLY raw JSON.
No markdown. No explanations. No text outside JSON.
Call CVE tool if severity is HIGH and no CVE ID is present.
Output format:
{
  "risk_level": "LOW | MEDIUM | HIGH",
  "call_cve_tool": true | false,
  "analysis_reason": "string"
}
"""

def analysis_agent(state: dict) -> dict:
    parsed_report = state["parsed_report"]
    retrieved_context = state.get("retrieved_context", [])

    user_prompt = f"""
Parsed Report:
{json.dumps(parsed_report, indent=2)}

Retrieved Context:
{json.dumps(retrieved_context, indent=2)}
"""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.2,
        max_tokens=300
    )

    text = response.choices[0].message.content.strip()

    try:
        result = json.loads(text)
    except json.JSONDecodeError:
        # PRODUCTION-SAFE FALLBACK
        result = {
            "risk_level": "LOW",
            "call_cve_tool": False,
            "analysis_reason": "Invalid model output; defaulted to LOW risk."
        }

    state["risk_level"] = result["risk_level"]
    state["call_cve_tool"] = result["call_cve_tool"]
    state["analysis_reason"] = result["analysis_reason"]

    return state
