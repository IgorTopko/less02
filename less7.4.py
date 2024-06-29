def common_elements():
    return set(num for num in range(1, 101) if num % 3 == 0) & set(num for num in range(1, 101) if num % 5 == 0)
result = common_elements()
print(result)