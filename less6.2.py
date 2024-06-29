seconds = int(input("Введіть кількість секунд: "))

days = seconds // (24 * 3600)
hours = (seconds % (24 * 3600)) // 3600
minutes = (seconds % 3600) // 60
seconds = seconds % 60

result = f"{days} день,{hours:02}:{minutes:02}:{seconds:02}"

print(result)