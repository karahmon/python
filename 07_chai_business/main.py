import recipes.flavours

print(recipes.flavours.ginger_chai())

from recipes.flavours import elaichi_chai
print(elaichi_chai())

#Dont use this method
# from .recipes.flavours import ginger_chai
# print(ginger_chai())