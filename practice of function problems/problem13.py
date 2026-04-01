def largest_number(l):
    max_value = l[0]

    for num in l:
        if num > max_value:
            max_value = num
    return max_value
l = [1, 23, 34,55,22,44,56,67]
print(largest_number(l))
    
