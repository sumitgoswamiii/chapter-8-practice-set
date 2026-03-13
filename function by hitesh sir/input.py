# problem 1
chai = "Ginger chai"
def prepare_chai(order):
    print("preparing", order)

prepare_chai(chai)
print(chai)

#problem 2
chai = [1, 2, 3]
def edit_chai(cup):
    cup[2] = 42

edit_chai(chai)
print(chai)

#problem 3
def make_chai(tea, milk, sugar):
    print(tea, milk, sugar)

make_chai("Darjeeling", "Yes", "Low") #positional
make_chai(tea = "Green", sugar = "Medium", milk = "No") #keywords

#problem 4
def special_chai(*ingredients, **extras):
    print("ingredients", ingredients)
    print("Extras", extras)

special_chai("cinnamon","cardamom",sweetener = "Honey", foam = "Yes")

#problem 5
def chai_order(order = []):
    order.append("Masala")
    order.append("cardamom")
    print(order)

chai_order()
# problem 6
def tea_order(order = None):
    if order is None:
        order = []
        print(order)

tea_order()
tea_order()



