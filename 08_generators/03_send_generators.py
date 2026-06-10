def chai_customer():
    print("What would you like to order?")
    order = yield
    while True:
        print(f"Preparing {order}...")
        order = yield
        
customer_gen = chai_customer()

next(customer_gen)

customer_gen.send("Masala Chai")
customer_gen.send("Lemon Chai")