def find_unique_value(one_list):
    for num in one_list:
        if one_list.count(num) == 1:
            return num
assert find_unique_value([1, 2, 1, 1]) == 2
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5
print("ОК")