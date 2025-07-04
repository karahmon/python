# dictionary to give position according to keys
chai_order = dict(type = "Masala Chai" , size = "Large" , sugar = 2)
print(f"Chai Order : {chai_order}")

chai_recipe = {}
chai_recipe["base"] = "green tea"
chai_recipe["liquid"] = "milk"

# to get partial element based on key
print(f"Recipe base : {chai_recipe['base']}")
print(f"Recipe : {chai_recipe}")

# to delete a key and pair
del chai_recipe["liquid"]
print(f"Recipe : {chai_recipe}")

#Membership Testing
print(f"Base is black tea ? : {"black tea" in chai_recipe['base']}")


chai_order = {"type" : "Ginger Chai" , "size" : "Medium" , "sugar" : 3}
print(f"Chai Order : {chai_order}")

# To get the keys
print(f"Order Details (keys) : {chai_order.keys()}")

# To get the values
print(f"Order Details (keys) : {chai_order.values()}")

# To get the items
print(f"Order Details (keys) : {chai_order.items()}") #will return tuples

#To remove the last item from the dictionary
last_item = chai_order.popitem()
print(f"Removed last item : {last_item}")

#to update existing dictionary with new values
extra_spices= {"cardamom" : "crushed" , "ginger" : "sliced"}
chai_recipe.update(extra_spices)
print(f"Updated Recipe : {chai_recipe}")

#to get info , if no info will giive default response
customer_note = chai_order.get("note","No Note")
print(f"Customer Note is : {customer_note}")
