# method 1
name = "sumit"
def user(name):
        return name[::-1]
print(user(name))

#  method 2
name = "sumit"
def user(name):
    reversed_name = ""

    for char in name:
        reversed_name = char + reversed_name

    return reversed_name
print(user(name))

# method 3
def step(name):
    reversed_name = ""

    for i in range(len(name)-1, -1, -1):
        reversed_name += name[i]

    return reversed_name
print(step("sumit"))
            
        
 
    