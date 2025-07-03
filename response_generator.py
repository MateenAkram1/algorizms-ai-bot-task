def generate_response(intent_data):
    intent = intent_data["intent"]
    if intent == "update_route":
        return f"Route updated to {intent_data['city']}."
    elif intent == "next_job":
        return "Your next job is picking up goods from Warehouse 14."
    elif intent == "next_delivery":
        return "Your next delivery is scheduled for tomorrow at 10 AM."
    elif intent == "cancel_job":
        return "Your current job has been cancelled."
    elif intent == "confirm_dropoff":
        return f"Drop-off in {intent_data['city']} confirmed."
    else:
        return "Sorry, I didn't understand that."
