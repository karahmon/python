menu = [
    "Masala Chai",
    "Ice Chai",
    "Peach Chai",
    "Green Tea",
    "Ice Peach Chai"
]

iced_tea = [tea for tea in menu if "Ice" in tea if len(tea) > 9]
print(iced_tea)