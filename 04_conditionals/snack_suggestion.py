order = input ("Enter your preferred snack : ").lower()
print(f"User Ordered : {order}")
if order == "samosa" or order == "cookies" :
    print("Order Confirmed")
else :
    print("Order Not Accepted")
