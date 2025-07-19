class Chai :
    origin  = "India" #properties   

print(Chai.origin)

Chai.is_hot = True
print(Chai.is_hot)

# creating objects from class chai
masala = Chai()
print(masala.origin)
print(masala.is_hot) 
masala.is_hot = False
print(masala.is_hot)
print(Chai.is_hot)
masala.flavour = "Elaichi"
print(masala.flavour)