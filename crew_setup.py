from crewai import Crew
from agents import crop_advisor, disease_expert, policy_advisor,priority_agent
from tasks import crop_task, disease_task, policy_task,priority_task

agriculture_crew = Crew(
    agents=[
        priority_agent,
        crop_advisor,
        disease_expert,
        policy_advisor
    ],

    tasks=[
        priority_task,
        crop_task,
        disease_task,
        policy_task
    ],

    verbose=True
)