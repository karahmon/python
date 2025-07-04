order_amount = int(input ("Enter order Amount : "))
delivery_fees = 0 if order_amount >300 else 30
print(f"Delivery Fees is : {delivery_fees}")

