# method 1
def get_even_numbers(lst):
    return [num for num in lst if num % 2 == 0]
print(get_even_numbers([1, 2, 3, 4, 8, 6, 5, 13, 16, 9]))

# method 2
def get_even_numbers(lst):
    even_list = []
    for num in lst:
        if num % 2 == 0:
            even_list.append(num)
    return even_list
number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(get_even_numbers(number))