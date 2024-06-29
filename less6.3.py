number = int(input("Введіть ціле число: "))

while number > 9:
    digits = [int(digit) for digit in str(number)]
    value = 1
    for digit in digits:
        value *= digit
    number = value
print(number)