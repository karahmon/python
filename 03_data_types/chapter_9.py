essential_Spices = {"cardamom","ginger","cinnamon"}
optional_Spices = {"cloves","ginger","black pepper"}

# \ - union removes duplicate items keeps only 1 present in both sets
all_spices = essential_Spices | optional_Spices
print(f"All Spices : {all_spices}")

# & - shows duplicate items present in both sets
common_spices = essential_Spices & optional_Spices
print(f"Common Spices : {common_spices}")

# - helps remove items present in both sets
only_in_essential = essential_Spices - optional_Spices
print(f"Essential Spices : {only_in_essential}")

#membership test
print(f"Is cloves an essential spice ? {"cloves" in essential_Spices}")
