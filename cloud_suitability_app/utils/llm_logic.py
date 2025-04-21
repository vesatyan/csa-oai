
def get_llm_reasoning(row):
    # Mock LLM-based reasoning. Replace with Azure OpenAI call in production.
    strategy = row.get("Migration Strategy", "Rehost")
    cost = row.get("OS Cost Score", 0)
    return f"The app is recommended for {strategy} due to criticality and cost score of {cost}."
