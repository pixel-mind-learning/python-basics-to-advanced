favourite_chais = [
    "Masala Chai",
    "Green Tea",
    "Masala Chai",
    "Green Tea",
    "Lemon Chai",
    "Ginger Chai",
]

unique_chais = {chai for chai in favourite_chais}
print(unique_chais)

recipes = {
    "Masala Chai": [
        "Boil water",
        "tea leaves",
        "add spices",
        "add milk",
        "and simmer.",
    ],
    "Green Tea": [
        "Boil water",
        "add green tea leaves",
        "steep for 2-3 minutes",
        "and strain.",
    ],
    "Lemon Chai": ["Boil water", "add tea leaves", "add lemon juice", "and simmer."],
    "Ginger Chai": [
        "Boil water",
        "add tea leaves",
        "add ginger slices",
        "add milk",
        "and simmer.",
    ],
    "Iced Lemon Tea": [
        "Boil water",
        "add tea leaves",
        "add lemon juice",
        "steep for 2-3 minutes",
        "strain and chill.",
    ],
}

unique_ingredients = {ingredient for ingredients in recipes.values() for ingredient in ingredients}

print(unique_ingredients)