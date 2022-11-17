a = int(input("Введите начало диапазона: "))
b = int(input("Введите конец диапазона: "))
summa = 0
while a <= b:
    if a % 2 == 1:
        summa += a
    a += 1
print("Сумма целых нечетных чисел:", summa)
