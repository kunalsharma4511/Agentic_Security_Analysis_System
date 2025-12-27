from typing import TypedDict, List, Dict, Any
from langgraph.graph import StateGraph, END

class SecurityState(TypedDict):
    raw_report: str
    parsed_report: Dict[str, Any]
    retrieved_context: List[Dict[str, Any]]
    risk_level: str
    call_cve_tool: bool
    analysis_reason: str
    recommendations: str

from agents.ingestion_agent.code import ingestion_agent
from agents.retrieval_agent.code import retrieval_agent
from agents.analysis_agent.code import analysis_agent
from agents.recommendation_agent.code import recommendation_agent

def build_graph():
    graph = StateGraph(SecurityState)

    # Add nodes
    graph.add_node("ingestion", ingestion_agent)
    graph.add_node("retrieval", retrieval_agent)
    graph.add_node("analysis", analysis_agent)
    graph.add_node("recommendation", recommendation_agent)

    # Define flow
    graph.set_entry_point("ingestion")
    graph.add_edge("ingestion", "retrieval")
    graph.add_edge("retrieval", "analysis")

    # Conditional routing after analysis
    graph.add_conditional_edges(
        "analysis",
        lambda state: "recommendation",  # CVE agent can be added later
        {
            "recommendation": "recommendation"
        }
    )

    graph.add_edge("recommendation", END)

    return graph.compile()



if __name__ == "__main__":
    app = build_graph()

    initial_state = {
        "raw_report": "SQL Injection vulnerability detected in Auth Service login API."
    }

    final_state = app.invoke(initial_state)

    print("\n=== FINAL OUTPUT ===")
    print("Risk Level:", final_state["risk_level"])
    print("Reason:", final_state["analysis_reason"])
    print("Recommendations:\n", final_state["recommendations"])
