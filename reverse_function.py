def my_reverse(my_list):
    reversed_list = []
    count = len(my_list)
    while len(my_list)!=len(reversed_list):
        reversed_list.append(my_list[count-1])
        count = count - 1
    return reversed_list

print(my_reverse([3,4,5,6]))
print(my_reverse([2,6,19,34]))