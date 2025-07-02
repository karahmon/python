#Integers 

sugar_grams = 3
teapowder_grams = 15

#Addition
total_grams = sugar_grams + teapowder_grams
print(f"Total grams : {total_grams}")

#Subtraction
sugarless_tea_grams = total_grams - sugar_grams
print(f"Total grams without Sugar : {sugarless_tea_grams}")

#Division
milk_litres = 5
total_servings = 7
milk_per_serving = milk_litres / total_servings
print(f"Total Milk Per Serving : {milk_per_serving}")

#Floor Division
total_teabags = 9
total_pots = 4 
teabags_per_pot = total_teabags // total_pots
print(f"Total Teabags Per Pot : {teabags_per_pot}") #floors the value useful where you dont need fractions

#Remainder 
total_pods = 10
pods_per_cup = 3
leftover_pods = total_pods % pods_per_cup
print(f"Total Pods Left : {leftover_pods}") #Displays Remainder of Division


#Multiples (Power)
base_flavour_strength = 2
scale_factor = 3
scale_flavour_strength = base_flavour_strength ** scale_factor
print(f"Scaled flavour Strength : {scale_flavour_strength}") # 2^3 power ( 2 * 2 * 2)

#For Readablity we can add _ to make numbers more readable
total_tea_leaves_harvested = 1_00_000
print(f"Total Number of Tea Leaves Harvested : {total_tea_leaves_harvested}") 