value = input('Введіть операцію (+, -, *, /): ')

num1 = int(input('Введіть перше число: '))
num2 = int(input('Введіть друге число: '))

if value == '+':
    print(num1 + num2)
elif value == '-':
    print(num1 - num2)
elif value == '*':
    print(num1 * num2)
elif value == '/':
    if num2 == 0:
        print('Помилка: Неправильна операція')
    else:
        print('Не можливо ділення на нуль')