#List - like array and mutable (can be changed)

ingredients = ["water","milk","black tea"]
print(f"Original Ingredients : {ingredients}")

#Append - to add a object at the end of the list 
ingredients.append("sugar")
print(f"Updated Ingredients : {ingredients}")

#Remove - to remove a particular object
ingredients.remove("sugar")
print(f"Removed Ingredients : {ingredients}")

spice_options = ["ginger","cardamom"]
chai_ingredients =["water","milk"]
print(f"Chai Ingredients : {chai_ingredients}")

#Extend - to add one list into another
chai_ingredients.extend(spice_options)
print(f"Combined Chai Ingredients : {chai_ingredients}")

#insert - adds object as per mentioned position
chai_ingredients.insert(1,"sugar")
print(f"Inserted Chai Ingredients : {chai_ingredients}")

#pop - removes an element based on the position given
chai_ingredients.pop(1)
print(f"Poped Chai Ingredients : {chai_ingredients}")

#Reverse - reverses the list
chai_ingredients.reverse()
print(f"Reversed Chai Ingredients : {chai_ingredients}")

#Sorts - sorts the list
chai_ingredients.sort()
print(f"Sorted Chai Ingredients : {chai_ingredients}")

#Max/Min - to find maximum and minimum
sugar_levels = [1,10,2,3,4,5]
print(f"Maximum Sugar level : {max(sugar_levels)}")
print(f"Maximum Sugar level : {min(sugar_levels)}")

#Operator Overloading - performs operations on list to make it easy instead of mentioning methods
base_liquid = ["water","milk"]
extra_flavor = ["ginger"]
full_liquid_mix = base_liquid + extra_flavor
print(f"Liquid Mix : {full_liquid_mix}")

strong_brew = ["black tea","ginger"] * 3
print(f"Liquid Mix : {strong_brew}")

raw_spice_data = bytearray(b"cinnamon")
print(f"Bytearray : {raw_spice_data}")
raw_spice_data = raw_spice_data.replace(b"cinn", b"card")
print(f"Bytearray : {raw_spice_data}")