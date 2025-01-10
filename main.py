# Python Modules and Data Handling : Your Mood Today - Problem Statement: Create a Python program using a custom module that asks the user how they are feeling today and 
# responds with a custom message based on the mood entered.

import mood_responses
mood = input("How are you feeling today? ")
print(mood_responses.mood_response(mood))

#Mastering Python Modules and Aliases Problem Statement: Create a custom module named `text_utils.py` with functions for string manipulation (e.g., reversing a string, capitalizing). 
# In your main script, import this module using an alias and utilize its functions.

import text_utils as script

s = input ("Enter the text you would like to reverse: ")
print(script.reverse_string(s))

s = input ("Enter the text you would like to capitalize: ")
print(script.capitalize_string(s))