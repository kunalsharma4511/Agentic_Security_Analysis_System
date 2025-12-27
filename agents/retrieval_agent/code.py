from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.documents import Document
# from google import genai
from dotenv import load_dotenv
load_dotenv()
# Initialize embedding model
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# ---- Mock Knowledge Base ----
documents = [
    Document(
        page_content="SQL Injection allows attackers to execute arbitrary SQL queries.",
        metadata={"severity": "HIGH", "type": "injection"}
    ),
    Document(
        page_content="Input validation and prepared statements help prevent SQL injection.",
        metadata={"severity": "HIGH", "type": "remediation"}
    ),
    Document(
        page_content="Brute force attacks involve repeated login attempts.",
        metadata={"severity": "MEDIUM", "type": "authentication"}
    ),
]

# Create vector store (in-memory)
vector_store = FAISS.from_documents(documents, embeddings)

def retrieval_agent(state: dict) -> dict:
    """
    LangGraph node: Retrieval Agent
    """
    parsed_report = state["parsed_report"]

    query = f"{parsed_report.get('issue')} in {parsed_report.get('component')}"
    
    results = vector_store.similarity_search(query, k=3)

    retrieved_context = [
        {
            "content": doc.page_content,
            "metadata": doc.metadata
        }
        for doc in results
    ]

    state["retrieved_context"] = retrieved_context
    return state
