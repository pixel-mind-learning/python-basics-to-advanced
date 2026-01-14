# value = 13
# remainder = value % 5

# if remainder:
#     print(f"Not divisable, remainder is {value}")

value = 13

if remmainder := value % 5:
    print(f"Not divisable, remainder is {remmainder}")

available_sizes = ["small", "medium", "large"]

if (requested_size := input(f"Enter your chai cup size: ")) in available_sizes:
    print(f"Serving {requested_size} chai")
else:
    print(f"Size is unavailble - {requested_size}")

flavours = ["masala", "ginger", "lemon", "mint"]

print(f"Available flavours: ", flavours)

while (flavour := input(f"Choos your flavour: ")) not in flavours:
    print(f"Sorry, {flavour} is not available")
print(f"You choose {flavour} chai")
