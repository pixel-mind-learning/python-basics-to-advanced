
# tuples

masala_spices = ("cardamon", "cloves", "cinnomon")

(spice1, spice2, spice3) = masala_spices

print(f"Main masala spices :{spice1}, {spice2}, {spice3}")

ginger_ratio, cardamon_ratio = 2, 1
print(f"G ratio is: {ginger_ratio} and C ratio is: {cardamon_ratio}")
ginger_ratio, cardamon_ratio = cardamon_ratio, ginger_ratio
print(f"After swapping, G ratio is: {ginger_ratio} and C ratio is : {cardamon_ratio}")

# membership test

print(f"Is ginger in masala spices ? {'cardamon' in masala_spices}")