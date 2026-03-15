from crew_setup import agriculture_crew

query = input("Enter agriculture question: ")

result = agriculture_crew.kickoff(
    inputs={"query": query}
)

print(result)