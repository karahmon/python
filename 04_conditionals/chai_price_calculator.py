input = input("Choose your cup size (small/medium/large) :- ").lower()
if input == "large" :
    print(f"Rs. 20")
elif input == "medium" : 
    print(f"Rs. 15")
elif input == "small" : 
    print(f"Rs. 10")
else :
    print(f"Unkown cup size")