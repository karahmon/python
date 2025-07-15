favourite_chais = [
    "Masala Chai",
    "Green Tea",
    "Masala Chai",
    "Lemon Tea",
    "Green Tea",
    "Elaichi Chai"
]

unique_chai = {chai for chai in favourite_chais}
print(unique_chai)

receipes = {
    "Masala Chai" : ["ginger","cardamom","clove"],
    "Elaichi Chai" : ["milk","cardemom"],
    "Masala Chai" : ["ginger","black pepper","clove"]
}

unique_spices = {spice for ingredients in receipes.values() for spice in ingredients}
print(unique_spices)