# method 1
def number(n):
    if(n%2 == 0):
        print(f"{n} is an even number")
    else:
        print(f"{n} is an odd number")
number(53)

# method 2
def check_even_or_odd(n):
    if n%2==0:
        return "Even"
    else:
        return "Odd"
print(check_even_or_odd(76))


