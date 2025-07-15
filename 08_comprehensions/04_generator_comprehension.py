daily_sales = []
x = 1
while len(daily_sales) < 100 :
    daily_sales.append(x)
    x += 1
print(daily_sales)

total_cups = sum(sale for sale in daily_sales if sale > 5)
print(total_cups)