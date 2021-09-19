#RECIPE IMPORTS
#Each recipe must be individually imported from cookbook
#Going to try and refine this to import a single JSON file
from cookbook import chickpea_chili
from cookbook import apple_crumb_cake

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

#Each recipe is assigned to a unique variable
a = Recipe(apple_crumb_cake)
b = Recipe(chickpea_chili)

#Terminal text to print user instructions
print(
'''
 ––––––––––––––––––––––––––––––––––––––––
|Enter the letter for your desired recipe|
| - - - - - - - - - - - - - - - - - - - -|
|a - apple crumb cake                    |
|b - chickpea chili                      |
| - - - - - - - - - - - - - - - - - - - -|
|x - exit                                |
 ––––––––––––––––––––––––––––––––––––––––
'''
)

#Terminal text asking the user for input
recipe = input("What do you want to cook? ")

#Loop which allows the user to input multiple recipies and combines them into a single dictionary called groceries_dict
while True:
    if recipe == "x":
        break
    elif recipe == "a":
        groceries_dict = Recipe(groceries_dict) + a
        recipe = input("What else do you want to cook? ")
    elif recipe == "b":
        groceries_dict = Recipe(groceries_dict) + b
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