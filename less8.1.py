def add_one(some_list):
    if not some_list:
        return [1]
    num = int(''.join(map(str, some_list))) + 1
    return list(map(int, str(num)))

assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5]
assert add_one([9, 9, 9]) == [1, 0, 0, 0]
assert add_one([0]) == [1]
assert add_one([9]) == [1, 0]
print("OK")