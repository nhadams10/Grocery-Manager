#RECIPE IMPORTS
#Imports all recipe dictionaries from cookbook
from cookbook import *
import os
from twilio.rest import Client

#This defines a recipe class which allows dictionaries to be added together
class Recipe(dict):
    def __add__(self, oth):
        r = self.copy()

        try:
            for key, val in oth.items():
                if key in r:
                    r[key] += val  # You can custom it here
                else:
                    r[key] = val
        except AttributeError:  # In case oth isn't a dict
            return NotImplemented  # The convention when a case isn't handled

        return r

#This is the empty dictionary we will use in our while loop
groceries_dict = {}



# 1. Each recipe is assigned to a unique variable
a = Recipe(apple_crumb_cake)
b = Recipe(chickpea_chili)
c = Recipe(tamari_lime_tempeh)
d = Recipe(red_lentil_pesto_pasta)

# 2. Terminal text to print user instructions
print(
'''
 ––––––––––––––––––––––––––––––––––––––––
|Enter the letter for your desired recipe|
| - - - - - - - - - - - - - - - - - - - -|
|a - apple crumb cake                    |
|b - chickpea chili                      |
|c - tamari lime tempeh                  |
|d - red lentil pesto pasta              |
| - - - - - - - - - - - - - - - - - - - -|
|x - exit                                |
 ––––––––––––––––––––––––––––––––––––––––
'''
)

#Terminal text asking the user for input
recipe = input("What do you want to cook? ")

# 3. Loop which allows user to input multiple recipies & combines them into a single dictionary called groceries_dict
while True:
    if recipe == "x":
        break
    elif recipe == "a":
        groceries_dict = Recipe(groceries_dict) + a
        recipe = input("What else do you want to cook? ")
    elif recipe == "b":
        groceries_dict = Recipe(groceries_dict) + b
        recipe = input("What else do you want to cook? ")
    elif recipe == "c":
        groceries_dict = Recipe(groceries_dict) + c
        recipe = input("What else do you want to cook? ")
    elif recipe == "d":
        groceries_dict = Recipe(groceries_dict) + d
        recipe = input("What else do you want to cook? ")
    else:
        print(
'''
- - - - - - - - - - - - - - - - - - - - -
Please enter a valid recipe or x to exit
- - - - - - - - - - - - - - - - - - - - -
'''
            )
        recipe = input("What else do you want to cook? ")

#print(recipe + " Is this correct?")
#this is a to be developed feature to confirm what the user wants to cook

#This converts output from a dictionary to a user-friendly list
def print_grocery_list(dct):
    print("---------------------")
    print("Grocery List:")
    print("")
    for item, amount in dct.items():
        print("{} {}".format(amount, item))
    print("---------------------")

#This prints the finalized grocery list
print_grocery_list(groceries_dict)

#Want to add a feature using an SMS API to send the user a text with their grocery list for ease of access in the supermarket

#Want to write a program that produces the grocery list as an output in a single string
def create_sms_grocery_list(dct):
    sms_grocery_list_body = "Grocery List:\n\n"
    for item, amount in dct.items():
        sms_grocery_list_body = sms_grocery_list_body + "-{} {}\n".format(amount, item)
    return sms_grocery_list_body

#print(create_sms_grocery_list(groceries_dict))

#ENV Variable not working, hard coded here
#YOUR_PHONE_NUMBER = '+82555'

#Twilio Magic
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body=create_sms_grocery_list(groceries_dict),
                     from_=SENDING_PHONE_NUMBER,
                     to=YOUR_PHONE_NUMBER
                 )

print(message.sid)