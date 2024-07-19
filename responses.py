from random import choice, randint # choice([array of strings])

def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    # REPLACE WITH RESPONSES
    if lowered == '':
        return ""
    elif "hello" in lowered:
        return "Hello there!"
    elif "chii roll dice" in lowered:
        return f"You rolled: {randint(1, 6)}"
    else: 
        return "Chiitan did not understand."