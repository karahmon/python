staff = [("Amit",16), ("Rahul",22), ("Bablu",30)]

for name,age in staff:
    if age >= 18:
        print(f"{name} is eligible to manage the stuff")
        break
else:
    print(f"No one is eligible to manage staff")