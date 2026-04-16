from crewai import Agent
from crewai.tools import BaseTool
# from langchain_groq import ChatGroq
from crewai import LLM
from rag_setup import retriever
from dotenv import load_dotenv
import os

load_dotenv()

llm = LLM(
    model="groq/llama-3.1-8b-instant",
    temperature=0.3,
    api_key=os.getenv("GROQ_API_KEY")
)

# llm = ChatGroq(
#     model="groq/llama-3.1-8b-instant",
#     temperature=0.3,
#     api_key=os.getenv("GROQ_API_KEY")
# )

class AgricultureSearchTool(BaseTool):

    name: str = "agriculture_search"
    description: str = "Search agriculture knowledge base"

    def _run(self, query: str) -> str:

        docs = retriever.get_relevant_documents(query)

        context = "\n".join([doc.page_content for doc in docs])

        return context


agri_tool = AgricultureSearchTool()

priority_agent = Agent(
    role="Priority Classifier",
    goal="Classify farmer query into Urgent, Normal, or Planning",
    backstory="Expert in understanding farmer problems and urgency level",
    llm=llm,
    verbose=True
)

crop_advisor = Agent(
    role="Crop Advisor",
    goal="Provide crop recommendations for farmers",
    backstory="An agricultural scientist helping farmers choose crops",
    tools=[agri_tool],
    llm=llm,
    verbose=True
)

disease_expert = Agent(
    role="Disease Expert",
    goal="Identify crop diseases and suggest treatment",
    backstory="A plant pathology expert helping farmers",
    tools=[agri_tool],
    llm=llm,
    verbose=True
)

policy_advisor = Agent(
    role="Policy Advisor",
    goal="Explain agriculture schemes and government policies",
    backstory="Expert in Indian agriculture subsidies and policies",
    tools=[agri_tool],
    llm=llm,
    verbose=True
)