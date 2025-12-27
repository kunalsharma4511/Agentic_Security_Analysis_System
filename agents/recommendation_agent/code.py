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
You are a cybersecurity remediation assistant.

Rules:
- Provide clear, actionable remediation steps.
- Tailor recommendations to the risk level.
- Use consistent numbered bullet points ONLY.
- Do NOT include markdown.
- Do NOT include explanations outside recommendations.
"""

def recommendation_agent(state: dict) -> dict:
    risk_level = state["risk_level"]
    retrieved_context = state.get("retrieved_context", [])
    analysis_reason = state.get("analysis_reason", "")

    user_prompt = f"""
Risk Level: {risk_level}

Analysis Summary:
{analysis_reason}

Security Context:
{json.dumps(retrieved_context, indent=2)}

Generate remediation steps.
"""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.3,
        max_tokens=400
    )

    recommendations = response.choices[0].message.content.strip()

    # Safe fallback
    if not recommendations:
        recommendations = "No specific remediation steps could be generated."

    state["recommendations"] = recommendations
    return state
