from crewai import Crew
from agents import crop_advisor, disease_expert, policy_advisor
from tasks import crop_task, disease_task, policy_task

agriculture_crew = Crew(
    agents=[
        crop_advisor,
        disease_expert,
        policy_advisor
    ],

    tasks=[
        crop_task,
        disease_task,
        policy_task
    ],

    verbose=True
)