def serve_char():
    yield "Cup 1: Masala Chai"
    yield "Cup 2: Ginger Chai"
    yield "Cup 3: Cardamom Chai"
    
stall = serve_char()

for cup in serve_char():
    print(cup)
    
def chai_list():
    return ["Cup 1: Masala Chai", "Cup 2: Ginger Chai", "Cup 3: Cardamom Chai"]

print(chai_list())

def chai_generator():
    yield "Cup 1: Masala Chai"
    yield "Cup 2: Ginger Chai"
    yield "Cup 3: Cardamom Chai"

gen = chai_generator()

print(chai_generator())
print(list(chai_generator()))
print(next(gen))
print(next(gen))
print(next(gen))
# print(next(gen)) # This will raise StopIteration error as there are no more items to yield.