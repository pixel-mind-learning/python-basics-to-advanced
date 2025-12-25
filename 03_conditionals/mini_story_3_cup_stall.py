cup_size = input("Enter preferred cup size (small/medium/large):").lower()
price = ""

if cup_size == "small":
    price = "Price is 10 rupees"
elif cup_size == "medium":
    price = "Price is 20 rupees"
elif cup_size == "large":
    price = "Price is 50 rupees"
else:
    price = "Unknown cup size!"

print(price)
