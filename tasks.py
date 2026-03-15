from crewai import Task
from agents import crop_advisor, disease_expert, policy_advisor

crop_task = Task(
    description="""
Farmer Question: {query}

Provide clear crop farming advice.

DO NOT generate search queries.
DO NOT output JSON.
Give a final answer for farmers.
""",

    expected_output="Clear farming advice including crop recommendations and farming practices.",

    agent=crop_advisor
)


disease_task = Task(
    description="""
Farmer Question: {query}

Identify possible crop diseases and treatments.

DO NOT generate search queries.
Provide a clear final explanation.
""",

    expected_output="Explanation of disease symptoms and treatment methods.",

    agent=disease_expert
)


policy_task = Task(
    description="""
Farmer Question: {query}

List government schemes that may help farmers.

Explain benefits simply.
""",

    expected_output="List of government agriculture schemes with short explanation.",

    agent=policy_advisor
)