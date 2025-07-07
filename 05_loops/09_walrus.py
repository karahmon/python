# value = 13
# remainder = value % 5

# if remainder :
#     print(f"Not divisble by 5, remainder is {remainder}")
    
value = 15
if (remainder := value % 5):
    print(f"Not divisble by 5, remainder is {remainder}")

available_sizes = ["small","medium","large"]
if(requsted_size := input("Enter your requsted size : ")) in available_sizes :
    print(f"Serving {requsted_size} chai")
else :
    print(f"Chai not availble in {requsted_size} cup")

flavours = ["masala","ginger","lemon","mint"]
print(f"These are available flavours with us :- {flavours}")

while (flavour := input("Choose Your Flavour :- "))not in flavours :
    print("Flavour not available please choose flavour from the list")
print (f"Order confirmed for {flavour} chai")