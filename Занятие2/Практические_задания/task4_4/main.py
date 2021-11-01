list_numbers = list(range(5, 17))

# TODO заменить значение 5-го элемента средним арифметическим
list_numbers[4] = sum(list_numbers) / len(list_numbers)
print(list_numbers)
