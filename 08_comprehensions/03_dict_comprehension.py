tea_prices_inr = {
    "Masala Chai" : 20,
    "Herbal Chai" : 40,
    "Mint Chai" : 60,
}

tea_prices_usd = {tea:price/80 for tea,price in tea_prices_inr.items()}
print(tea_prices_usd)