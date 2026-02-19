# problem 1
for token in range(1,11):
    print(f"Serving chai to token:{token}")

# problem 2
for batch in range(1,5):
    print(f"preparing chai for batch: #{batch}")

# problem 3
def multiplication_table(number: int) -> list[str]:

    result = []
    for i in range(1,11):
        result.append(f"{number} x {i} = {number * i}")
    return result

# problem 4
order = ["Hitesh","Aman","sumit","carlos","becky"]

for name in order:
    print(f"Order ready for: {name}")

# problem 5
menu = ["Green","Lemon","Spiced","Mint"]
for i, item in enumerate(menu, start=1):
    print(f"{i}:{item} tea")

# problem 6
names = ["sumit","Hitesh","sam","ankur","anish"]
bills = [78,57,36,53,45]
for name,amount in zip(names, bills):
    print(f"{name} paid {amount} rupees")
