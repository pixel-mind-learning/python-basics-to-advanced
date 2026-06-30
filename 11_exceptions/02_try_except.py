chai_menu = {"masala": 30, "ginger": 40}

try:
    chai_menu["elaichi"]

except KeyError:
    print("The key that you are trying to access dooes not exists")

finally:
    print("Resources are closed")

print("Hello chai code")
