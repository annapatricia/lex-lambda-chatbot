def close(message: str) -> dict:
    """Finish the conversation with a final message."""
    return {
        "sessionState": {
            "dialogAction": {"type": "Close"},
            "intent": {"state": "Fulfilled"},
        },
        "messages": [{"contentType": "PlainText", "content": message}],
    }


def elicit_slot(slot_to_elicit: str, message: str, slots: dict, intent_name: str) -> dict:
    """Ask the user for a missing slot."""
    return {
        "sessionState": {
            "dialogAction": {"type": "ElicitSlot", "slotToElicit": slot_to_elicit},
            "intent": {"name": intent_name, "slots": slots, "state": "InProgress"},
        },
        "messages": [{"contentType": "PlainText", "content": message}],
    }
