def infinite_chai():
    cup_number = 1
    while True:
        yield f"Cup {cup_number}: Masala Chai"
        cup_number += 1

infinite_chai_gen = infinite_chai()
user1 = infinite_chai()

for _ in range(5):
    print(next(infinite_chai_gen))
    
for _ in range(7):
    print(next(infinite_chai_gen))
    
for _ in range(5):
    print(next(user1))