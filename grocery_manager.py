from cookbook import chickpea_chili
from cookbook import apple_crumb_cake

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

groceries_dict = Recipe({})

a = Recipe(apple_crumb_cake)
b = Recipe(chickpea_chili)

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

recipe = input("What do you want to cook? ")

while True:
    #recipe = input("What do you want to cook?")
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
#this should be updated to confirm what the user wants to cook

#groceries_dict = a + b
# this should be updated to responsively create a dictionary for all the needed groceries

grocery_list = '''
6 Apples
5 Oranges
'''
#this should be updated to convert output from a dictionary to a user-friendly list

print(groceries_dict)