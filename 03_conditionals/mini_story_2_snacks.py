snack = input("Enter your prefferred snack: ").lower()

print(f"user said: {snack}")


if snack == "cookies" or snack == "samosa":
    print(f"Great choice! We'll serve you {snack}")
else:
    print(f"Sorry, we only serve cookies or samosa with tea.")
