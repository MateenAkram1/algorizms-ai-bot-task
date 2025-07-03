import re

def parse_intent(text):
    text = text.lower()

    match = re.match(r"update my route to (\w+)", text)
    if match:
        return {"intent": "update_route", "city": match.group(1)}

    if "next job" in text:
        return {"intent": "next_job"}

    if "next delivery" in text:
        return {"intent": "next_delivery"}

    if "cancel my current job" in text:
        return {"intent": "cancel_job"}

    match = re.match(r"confirm drop[- ]?off in (\w+)", text)
    if match:
        return {"intent": "confirm_dropoff", "city": match.group(1)}

    return {"intent": "unknown"}
