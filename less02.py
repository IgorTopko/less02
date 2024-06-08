value_1 = int(input("Введіть 5-x значне число: "))

numb_1 = value_1 % 10 * 10000
numb_2 = value_1 % 100 // 10 * 1000
numb_3 = value_1 % 1000 // 100 * 100
numb_4 = value_1 % 10000 // 1000 * 10
numb_5 = value_1 % 100000 // 10000

print (numb_1 + numb_2 + numb_3 + numb_4 + numb_5)
