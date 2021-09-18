from recipes import chickpea_chili_recipe
from recipes import apple_crumb_cake_recipe

#recipe = input("What do you want to cook? ")
#print(recipe + " Is this correct?")

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

a = Recipe(apple_crumb_cake_recipe)
b = Recipe(chickpea_chili_recipe)
c = a + b

print(c)