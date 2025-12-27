from agents.retrieval_agent.code import retrieval_agent
from dotenv import load_dotenv
load_dotenv()

def test_retrieval_agent():
    state = {
        "parsed_report": {
            "component": "Auth Service",
            "issue": "SQL Injection",
            "severity_hint": "HIGH"
        }
    }

    updated_state = retrieval_agent(state)

    print("Retrieved Context:")
    for item in updated_state["retrieved_context"]:
        print("-", item)

if __name__ == "__main__":
    test_retrieval_agent()
