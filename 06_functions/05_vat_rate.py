def add_vat(price,vat_rate):
    return price * (100+ vat_rate )/100

orders = [100,200,150]

for order in orders:
    final_amount = add_vat(order,10)
    print(f"Original Amount is {order} and Total Amount is {final_amount}")