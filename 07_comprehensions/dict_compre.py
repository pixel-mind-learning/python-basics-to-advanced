tea_prices_lkr = {
    "Masala Chai": 150,
    "Green Tea": 120,
    "Lemon Chai": 130,
    "Ginger Chai": 140,
    "Iced Lemon Tea": 160,
}

tea_calculated_prices = {tea: price * 0.5 for tea, price in tea_prices_lkr.items()}

print(tea_calculated_prices)
