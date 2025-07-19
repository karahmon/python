class Chai :
    temperature = "Hot"
    strength = "Strong"

cutting = Chai()
print(cutting.temperature)

cutting.temperature = "Mild"
cutting.cup = "Small"
print(f"After Changing : {cutting.temperature}")
print(f"Cup Size : {cutting.cup}")
print(f"Direct Look into the Class : {Chai.temperature}")

del cutting.temperature
del cutting.cup

print (f"After Deleting : {cutting.temperature}") # will print default of the class intialisation
#print (cutting.cup) wont work as there is no default value in class and deleted here so will return error
