def find_even(numbers):
    for num in numbers:

        if num % 2 == 0:
            print(num, "is an even")
            
        else:
            print(num,"is an odd")
            
numbers = [23, 12, 34, 55, 32, 22, 76, 67, 88]
print(find_even(numbers))