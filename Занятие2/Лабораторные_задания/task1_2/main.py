A = int(input("Введите число: "))
B = int(input("Введите число: "))

cond1 = A % 2 == 0  # Число А - четное
cond2 = B % 2 == 0  # Число B - четное

not (cond1 and cond2)
"не (Число А - четное и Число B - четное)"

not cond1 and not cond2
not(cond1 or cond2)
"""
не (a и b) = (не a) или (не b)
не (a или b) = (не a) и (не b)
"""

