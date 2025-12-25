essential_spices = {"cardamon", "ginger", "cinnamon"}
optional_spices = {"cloves", "ginger", "black pepper"}

# | Union
all_spices = essential_spices | optional_spices
print(f"All spices: {all_spices}")

# & Intersection
common_spices = essential_spices & optional_spices
print(f"Common spices: {common_spices}")

# - Difference
only_in_essential = essential_spices - optional_spices
print(f"Spices only in essential: {only_in_essential}")

# membership test
print(f"Is 'cloves' an essential spice? {'cloves' in essential_spices}")
print(f"Is 'cloves' an optional: {'cloves' in optional_spices}")

# set and frozenset exactly same except frozenset is immutable
frozen_essential_spices = frozenset(essential_spices)
print(f"Frozen essential spices: {frozen_essential_spices}")
