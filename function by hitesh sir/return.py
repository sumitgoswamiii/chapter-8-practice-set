# problem 1
def make_chai():
    return "Here is your masala chai"
return_value = make_chai()
print(return_value)

#problem 2
def idle_chaiwala():
    pass
print(idle_chaiwala())

#problem 3
def sold_cup():
    return 120
total = sold_cup()
print(total)

# problem 4
def chai_status(cups_left):
    if cups_left == 0:
        return "sorry, chai over"
    return "chai is ready"
print(chai_status(0))
print(chai_status(1))

#problem 5
def chai_report():
    return 100 ,20 # sold , remaining
sold, remaining = chai_report()
print("sold:",sold)
print("remaining:", remaining)


    

