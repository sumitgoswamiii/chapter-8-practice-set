# method 1
# L = [1,2,3,4]
# def sum_of_array(L):
#     return sum(L)
# print(sum_of_array(L))

#method 2
arr = [1,3,5,7,9]
def sum_array(arr):
    total = 0
    for num in arr:
        total += num
    return total 
print(sum_array(arr))