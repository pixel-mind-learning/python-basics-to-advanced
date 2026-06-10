chai = "Ginger chai"
def prepare_chai(order):
    print("Preparing ", order)

prepare_chai(chai)

def make_chai(tea, milk, sugar):
    print(tea, milk, sugar)

make_chai("Darjeeling", "Yes", "Low") #positional
make_chai(tea="Green", sugar="Medium", milk="No") #keywords

# args: arguments
# kwargs: key_value_arguments
def special_chai(*ingredients, **kwargs):
    print("Ingredients", ingredients)
    print("Extras", kwargs)

special_chai("Cinnamon", "Cardmom", sweetener="Honey", foam="yes")

# def chai_order(order = []):
#     order.append("Masala")
#     print(order)

def chai_order(order = None):
    if order is None:
        order = []
    print(order)

chai_order()
chai_order()
