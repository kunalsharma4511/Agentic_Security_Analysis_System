from agents.recommendation_agent.code import recommendation_agent

def test_recommendation_agent():
    state = {
        "risk_level": "HIGH",
        "analysis_reason": "SQL Injection vulnerability detected in authentication service.",
        "retrieved_context": [
            {
                "content": "SQL Injection allows attackers to manipulate database queries.",
                "metadata": {"severity": "HIGH"}
            },
            {
                "content": "Prepared statements and input validation mitigate SQL injection.",
                "metadata": {"type": "remediation"}
            }
        ]
    }

    updated_state = recommendation_agent(state)

    print("Recommendations:")
    print(updated_state["recommendations"])

if __name__ == "__main__":
    test_recommendation_agent()