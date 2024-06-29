import string

input_str = input("Введіть дві літери через дефіс: ")

start, end = input_str.split('-')
start_index = string.ascii_letters.index(start)
end_index = string.ascii_letters.index(end)

result = string.ascii_letters[start_index:end_index + 1]
print(result)