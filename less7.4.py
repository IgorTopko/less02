def common_elements():
    return set(num for num in range(1, 100) if num % 3 == 0) & set(num for num in range(1, 100) if num % 5 == 0)
result = common_elements()
print(result)
assert common_elements()