value = input("Введіть операцію (+, -, *, /): ")

num1 = int(input("Введіть перше число: "))
num2 = int(input("Введіть друге число: "))

if num2 == 0:
    print('Помилка: Ділення на нуль неможливе')
elif (value == '+'):
    print(num1 + num2)
elif value == '-':
    print(num1 - num2)
elif value == '*':
    print(num1 * num2)
elif value == '/':
    print(num1 / num2)
else:
    result == num1 / num2
    print ('result')



