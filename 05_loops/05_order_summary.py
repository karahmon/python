names = ["Sam","Altman","Ilya","Andrew"]
orders = [50,70,90,100]

for name,amount in zip(names,orders):
    print(f"{name} paid {amount} rupees")