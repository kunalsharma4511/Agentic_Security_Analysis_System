from agents.ingestion_agent.code import ingestion_agent
from dotenv import load_dotenv
load_dotenv()
def test_ingestion_agent():
    state = {
        "raw_report": """
        Application: Auth Service
        Issue: SQL injection in login API
        Severity: High
        Description: User input is not sanitized.
        """
    }

    updated_state = ingestion_agent(state)

    print("Parsed Report:")
    print(updated_state["parsed"])


if __name__ == "__main__":
    test_ingestion_agent()