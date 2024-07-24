from random import choice, randint # choice([array of strings])

def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    # REPLACE WITH RESPONSES
    if lowered == '':
        return ""
    elif "hello" in lowered:
        return "Hello there!"
    elif "help" in lowered:
        return '''
Chiitan ちぃたん☆ can do anything! Try:
!c football
!c roll'''
    elif "roll" in lowered:
        return f"You rolled: {randint(1, 6)}"
    elif "football" in lowered:
        return "https://tenor.com/view/chiitan-mascot-gif-26497375"
    elif "tennis" in lowered:
        return "https://tenor.com/view/chiitan-mascots-funny-gif-matchingpfp-gif-26459749"
    elif "dance friend" in lowered:
        return "https://tenor.com/lduBA9zP8I3.gif"
    elif "beat" in lowered:
        return "https://tenor.com/view/bobatyun-chiitan-gif-20581055"
    elif "acrobat" in lowered:
        return "https://tenor.com/view/chiitan-turtle-fall-falling-trick-gif-5224690783547185432"
    elif "magic trick" in lowered:
        return "https://tenor.com/bXdZ0.gif"
    else: 
        return "Chiitan did not understand."
    
def help():
    return '''
    ちぃたん☆ can do anything! Try:'''
    