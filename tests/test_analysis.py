from agents.analysis_agent.code import analysis_agent

def test_analysis_agent():
    state = {
        "parsed_report": {
            "component": "Auth Service",
            "issue": "SQL Injection",
            "severity_hint": "HIGH",
            "cve_id": None,
            "summary": "SQL injection vulnerability in login API"
        },
        "retrieved_context": [
            {
                "content": "SQL Injection allows attackers to execute arbitrary SQL queries.",
                "metadata": {"severity": "HIGH"}
            },
            {
                "content": "Prepared statements prevent SQL injection.",
                "metadata": {"type": "remediation"}
            }
        ]
    }

    updated_state = analysis_agent(state)

    print("Risk Level:", updated_state["risk_level"])
    print("Call CVE Tool:", updated_state["call_cve_tool"])
    print("Reason:", updated_state["analysis_reason"])

if __name__ == "__main__":
    test_analysis_agent()
