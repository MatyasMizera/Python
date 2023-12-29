def list_swap(list, old_num, new_num):
    for i in range(len(list)):
        if list [i] == old_num:
            list[i] = new_num
    return list
print(list_swap([2,5,8,5,2,5,7,5], 5, 11))  