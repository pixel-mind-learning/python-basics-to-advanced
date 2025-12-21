is_boiling = True
stri_count = 5
total_actions = stri_count + is_boiling # upcasting bool to int
print(f"Total actions (bool + int): {total_actions}")

milk_present = 0 # no milk
print(f"Is there milk? {bool(milk_present)}")

water_hot = True
tea_added = True

can_serve = water_hot and tea_added
print(f"Can we serve tea? {can_serve}")