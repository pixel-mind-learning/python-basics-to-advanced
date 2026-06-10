daily_sales = [4, 9, 3, 8, 9, 50, 60, 70, 4, 2, 1, 6]

total_sales = sum(cups for cups in daily_sales if cups > 5)

print(total_sales)