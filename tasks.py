from crewai import Task
from agents import crop_advisor, disease_expert, policy_advisor,priority_agent


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

Explain government schemes in simple language.

Do NOT output JSON
Do NOT use structured format like lists with symbols

Example:
You can apply for PM-KISAN scheme which gives financial support to farmers. Also, you may benefit from crop insurance schemes.

Now generate answer:
""",
    expected_output="Simple explanation of schemes in paragraph.",
    agent=policy_advisor
)


priority_task = Task(
    description="""
Analyze the farmer query and classify it into ONE category:

- Urgent → if disease, pest, sudden damage
- Normal → general farming advice
- Planning → schemes, profit, crop selection

Return ONLY one word:
Urgent OR Normal OR Planning

Farmer Question:
{query}
""",
    expected_output="One word: Urgent or Normal or Planning",
    agent=priority_agent
)