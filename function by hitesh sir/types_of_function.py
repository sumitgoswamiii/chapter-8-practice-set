def pure_chai(cups):  # this is a pure function because we don't add on this any external keywords.
    return cups * 10

total_chai = 0

def impure_chai(cups):   # this is a impure function because we use global keyword for call the total_chai,which is out side of the function
    global total_chai
    total_chai += cups

#problem 1
def pour_chai(n):
    print(n)
    if n==0:
        return "All cups poured"
    return pour_chai(n-1)
print(pour_chai(3))

# problem 2
chai_type = ["light", "strong", "ginger","cardamom", "tulsi","ginger"]

strong_chai = list(filter(lambda chai: chai !="ginger",chai_type))
print(strong_chai)

#problem 4
def square_list(nums: list[int])-> list[int]:
    return list(map(lambda n:n**2, nums))
print(square_list([1,2,3,4,5]))
    
