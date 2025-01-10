# Task 1: Your Mood Today - Problem Statement: Create a Python program using a custom module that asks the user how they are feeling today and 
# responds with a custom message based on the mood entered.

def mood_response(mood):
    mood = mood.lower()
    if mood == "happy":
        return "\n Knowing you are happy makes my heart smile. "
    elif mood == "sad":
        return "\n I'm sorry you are sad. If you want to talk about it I'll listen. "
    elif mood == "angry":
        return "\n What would you like to do to blow off some steam? "
    elif mood == "bored":
        return "\n Do you want to build a snow man? "
    elif mood == "tired":
        return "\n Try and get to be a little earlier tonight. "
    else:
        return "\n Please enter a valid response. "
        