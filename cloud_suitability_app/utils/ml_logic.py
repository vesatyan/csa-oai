
def get_strategy_prediction(row):
    # Simulated strategy prediction based on business & technical features
    if row.get("Business Criticality", "").lower() == "high":
        return "Replatform"
    elif row.get("App Load Predictability", "").lower() == "low":
        return "Retire"
    return "Rehost"

def calculate_cost_score(row):
    os = row.get("Operating System", "").lower()
    if "windows" in os:
        return 2  # Assume higher cost
    elif "linux" in os:
        return 1  # Assume lower cost
    return 3  # Unknown
