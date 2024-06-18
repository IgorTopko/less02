import random

my_list = random.randint(3, 10)
value_list = [random.randint(1, 1000) for _ in range(my_list)]
print(value_list)
if len(value_list) >= 3:
    new_list = [value_list[1], value_list[2], value_list[-2]]
    print(new_list)
else:
    print('end')