from recipes import chickpea_chili_recipe
from recipes import apple_crumb_cake_recipe
#from collections import defaultdict
from collections import Counter

#recipe = input("What do you want to cook? ")
#print(recipe + " Is this correct?")

A = Counter(chickpea_chili_recipe)
B = Counter(apple_crumb_cake_recipe)
#print (A + B)

C = A + B
#dd = defaultdict(list)

#for d in (chickpea_chili_recipe, apple_crumb_cake_recipe):
#  for key, value in d.items():
#    dd[key].append(value)

#groceries = {}

#for d in (chickpea_chili_recipe, apple_crumb_cake_recipe):
  
print(C)
#print(chickpea_chili_recipe['chickpea cans'])
#print(dd)
