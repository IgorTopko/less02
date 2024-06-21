while True:
    value = input("Введіть операцію (+, -, *, /): ")
    num1 = float(input("Введіть перше число: "))
    num2 = float(input("Введіть друге число: "))

    result = None

    if value not in ("+,-,*,/"):
        result = ("Помилка: Неправильна операція")
    elif value == "+":
        result = num1 + num2
    elif value == "-":
        result = num1 - num2
    elif value == "*":
        result = num1 * num2
    elif value == "/" and num2 == 0:
        result = ("Не можливо ділення на нуль")
    elif value == "/":
        result = num1 / num2
    print(result)
    calculator = input("Продовжити роботу калькулятора? (yes/no): ")
    if calculator == "yes":
        continue
        print("Робота калькулятора завершена")
    break