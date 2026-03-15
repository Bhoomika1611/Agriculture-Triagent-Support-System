from crewai import Agent
from crewai.tools import BaseTool
from langchain_groq import ChatGroq
from rag_setup import retriever
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
    model="groq/llama-3.1-8b-instant",
    temperature=0.3
)

class AgricultureSearchTool(BaseTool):

    name: str = "agriculture_search"
    description: str = "Search agriculture knowledge base"

    def _run(self, query: str) -> str:

        docs = retriever.get_relevant_documents(query)

        context = "\n".join([doc.page_content for doc in docs])

        return context


agri_tool = AgricultureSearchTool()


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