import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))





import streamlit as st

from workflow.graph import build_graph

# Page config
st.set_page_config(
    page_title="Agentic Security Analysis System",
    layout="centered"
)

st.title("🛡️ Agentic Security Analysis System")
st.write(
    "Analyze security reports using a multi-agent AI system with RAG and decision logic."
)

# Text input
raw_report = st.text_area(
    "Paste Security Report",
    height=200,
    placeholder="Example: SQL Injection vulnerability detected in Auth Service login API."
)

analyze_button = st.button("🔍 Analyze Report")

if analyze_button:
    if not raw_report.strip():
        st.warning("Please enter a security report.")
    else:
        with st.spinner("Running agentic analysis..."):
            app = build_graph()

            initial_state = {
                "raw_report": raw_report
            }

            final_state = app.invoke(initial_state)

        st.success("Analysis Complete")

        # Output section
        st.subheader("📊 Risk Assessment")
        st.write(f"**Risk Level:** {final_state['risk_level']}")
        st.write(f"**Reason:** {final_state['analysis_reason']}")

        st.subheader("🛠️ Recommendations")
        st.text(final_state["recommendations"])
