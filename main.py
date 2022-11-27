# name = "Elena"
# print("Hello world!!!", name)
# age = 20
# print(age)
# print(type(name))
# print(type(age))
# a = 4
# b = 5
# a = b
# print(id(a))  # id
# print(id(b))

# a = b = c = 1
# print(a, b, c)

# a, b, c = 5, "Hello", 9.2
# print(a, b, c)
# name = "Bob"
# print(name)

# PI = 3.14
# print(PI)
# PI = 5
# print(PI)

# name = "Den"
# age = 20
# print("Меня зовут: " + name + ". Мне " + str(age) + " лет.")
#
# a = 1
# b = 2
#
# print("a:", a)
# print("b:", b)
#
# # c = a
# # a = b
# # b = c
#
# # a, b = b, a
#
# print("a:", a)
# print("b:", b)

# print("строка \
# символов")
# print('строка')
#
# print("Документ \"script.py\" находится по заданному пути \nD:\\\Python\\Project")

# s1 = "Hello"
# s2 = "Python"
# s3 = s1 + ", " + s2 + "!\t\t"
# print(s3 * 3)
# print("*" * 20)

# print(416485444444444568)
# print(2.58948548648888888865132)

# print(6 + 2)
# print(6 - 2)
# print(6 * 2)
# print(6 / 2)  # При делении всегда получаем вещественное число
# print(7 / 2)  # 3.5
# print(6 // 2)  # 3
# print(7 // 2)  # 3
# print(7 % 2)  # 1
# print(7 ** 2)

# num = 10
# num +=5 #
# print(num)
#
# num = 4321
# a = num % 10
# print(a)
# num = num // 10
# b = num % 10
# print(b)
# num = num // 10
# c = num % 10
# print(c)
# num = num // 10
# d = num % 10
# print(d)
# print(a*1000 + b*100 + c*10 + d)
#
# num1 = 4321
# print(num1)
# res = (num1 % 10) * 1000
# num1 = num1 // 10
# res += (num1 % 10) * 100
# num1 = num1 // 10
# res += (num1 % 10) * 10
# num1 = num1 // 10
# res += (num1 % 10)
# print(res)

# int() - преобразует к целочисленному типу данных ###
# float() - преобразует к вещ-ому типу данных ###

# num1 = "2"
# num2 = 3
# res = int(num1) + num2
# print(res)
# print(int(3.8))
# print(round(3.891))
# print(round(3.891, 2))

# a = 5 / 3
# print(round(a, 2))

# a = "5.2"
# b = 10
# c = float(a) + b
# print(c)

# a = 1
# b = 2
# print("a: ", a, "\nb: ", b)

# name = "Виктор"
# age = 28
# print("Меня зовут: ", name, ". Мне ", age, "лет.")
# print("Меня зовут: " + name + ". Мне " + str(age) + "лет.")
# print("Меня зовут: ", name, ". Мне ", age, "лет.", sep="-aa-", end="\n\n")
# print("я убежал в лес.")

# name = input("Ваше имя: ")
# city = input("Ваш город: ")
# print(name, city)

# num1 = int(input("Введите число: "))
# step = int(input("Введите степень: "))
# c = num1 ** step
# print("Число", num1, "в степени", step, "равно", c)

# print("Введите четыре числа: ")
# a = int(input("1: "))
# b = int(input("2: "))
# c = int(input("3: "))
# d = int(input("4: "))
# sum1 = a + b
# sum2 = c + d
#
# del1 = sum1 / sum2
# print("Результат:", round(del1, 2))

# a = True
# b = False
# print(a + 5)  # 1 + 5
# print(b + 5)  # 0 + 5

# print(bool("python"))  # True
# print(bool(""))  # False
# print(bool(" "))  # True
# print(bool(0))  # False
# print(bool(1))  # True
# print(bool(0.0))  # False
# print(bool(False))  # False
# print(bool(None))  # False

# test = None
# print(test)
# test = 5
# print(test)

# print(7 == 7)
# print(2 + 5 != 7)
# print(8 > 7)
# print(8 < 7)
# print(8 <= 7)
# print("привет" == "Привет")

# print(2 < 4 < 9)
# print(2 * 5 > 7 >= 4 + 3)
# print(3 * 3 <= 7 >= 2)

# a = 10
# b = 5
# c = a == b
# print(a, b, c)  # 10, 5 , False

# print(5 - 3 == 2 and 1 + 3 == 4)  # True (True : True)
# print(5 - 3 == 2 and 1 + 3 < 4)  # False (True : False)
# print(5 - 3 > 2 and 1 + 3 == 4)  # False (False : True)
# print(5 - 3 > 2 and 1 + 3 < 4)  # False (False : False)

# print(5 - 3 == 2 or 1 + 3 == 4)  # True (True : True)
# print(5 - 3 == 2 or 1 + 3 < 4)  # True (True : False)
# print(5 - 3 > 2 or 1 + 3 == 4)  # True (False : True)
# print(5 - 3 > 2 or + 3 < 4)  # False (False : False)

# print(not 9 - 7)
# print(not 7 - 7)

# cnt = 15
# if cnt < 10:
#     cnt += 1
# print(cnt)

# age = int(input("Введите свой возраст: "))
# if age >= 18:
#     print("Доступ есть!")
# else:
#     print("Нет")

# a = 15
# b = 15
# if a > b:
#     print("a > b")
# elif a < b:
#     print("b > a")
# else:
#     print("b == a")

# a = int(input("Введите первую сторону: "))
# b = int(input("Введите вторую сторону: "))
# c = int(input("Введите третью сторону: "))
#
# if a == b == c:
#     print("Треугольник равносторонний")
# elif a == b or a == c or b == c:
#     print("Треугольник равнобедренный")
# else:
#     print("Треугольник разносторонний")

# m = int(input("Введите номер месяца: "))
# # if (m >= 1) and (m <= 12):
# if 1 <= m <= 12:
#     if m == 1 or m == 2 or m == 12:
#         print("Зима")
#     if m == 3 or m == 4 or m == 5:
#         print("Весна")
#     if m == 6 or m == 7 or m == 8:
#         print("Лето")
#     if m == 9 or m == 10 or m == 11:
#         print("Осень")
# else:
#     print("Такого месяца нет")
#
# day = int(input("Введите день недели (цифрой): "))
# if 1 <= day <= 5:
#     print("Рабочий день - ", end="")
#     if day == 1:
#         print("Понедельник")
#     if day == 2:
#         print("Вторник")
#     if day == 3:
#         print("Среда")
#     if day == 4:
#         print("Четверг")
#     if day == 5:
#         print("Пятница")
# elif day == 6 or day == 7:
#     print("Выходной день - ", end="")
#     if day == 6:
#         print("Суббота")
#     if day == 7:
#         print("Воскресенье")
# else:
#     print("Такого дня недели нет")

# n = int(input("Введите количество ворон: "))
# if 0 <= n <= 9:
#     print("На ветке ", end="")
#     if n == 1:
#         print(n, "ворона")
#     elif 2 <= n <= 4:
#         print(n, "вороны")
#     else:
#         print(n, "ворон")
#     # if n == 1:
#     #     print(n, "ворона")
#     # if 2 <= n <= 4:
#     #     print(n, "вороны")
#     # if 5 <= n <= 9 or n == 0:
#     #     print(n, "ворон")
# else:
#     print("Ошибка")

# a = int(input("Введите число от 1 до 99: "))
# kop = a
# if 11 <= kop <= 14:
#     print(a, "копеек")
# else:
#     kop = kop % 10
#     if kop == 1:
#         print(a, "копейка")
#     elif 2 <= kop <= 4:
#         print(a, "копейки")
#     else:
#         print(a, "копеек")

########### Тернарное выраженние ############

# a, b = 30, 20
# minim = a if a < b else b
# print(minim)

# a, b = 20, 30
# print("a == b" if a == b else "a > b" if a > b else "b > a")
# if a == b:
#     print("a == b")
# else:
#     if a > b:
#         print("a > b")
#     else:
#         print("b > a")

# a, b = 5, 2
# print("на ноль делить нельзя" if b == 0 else a / b)

#### Исключения

# a = 5
# b = 0
# print(a / b)

# try:
#     n = int(input("Введите целое число: "))
#     print(n * 2)
# except ValueError:
#     print("Что -то пошло не так")
#
# print("Код далее")

# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except ValueError:
#     print("Нельзя вводить строки")
# except ZeroDivisionError:
#     print("Нельзя делить на ноль")
# else:  # выполняется когда в try не возникло исключения
#     print("Все нормально. Вы ввели числа", n, "и", m)
# finally:  # выполняется в любом случае
#     print("Конец программы")

# n = input("Введите первое число: ")
# m = input("Введите второе число: ")
# try:
#     print(int(n) + int(m))
# except ValueError:
#     print(str(n) + str(m))
# либо
# n = input("Введите первое число: ")
# m = input("Введите второе число: ")
# try:
#     n = int(n)
#     m = int(m)
# except ValueError:
#     n = str(n)
#     m = str(m)
# finally:
#     print(n + m)

# i = 0
# while i < 5:
#     print("i =", i)
#     i += 1


# i = 10
# while i > 0:
#     print("i =", i)
#     i -= 1

# i = 1
# while i <= 20:
#     if i % 2 == 0:
#         print(i)
#     i += 1
# либо
# i = 0
# while i < 20:
#     i += 2
#     print(i)

# n = int(input("Укажите количество:"))
# i = 0
#
# while i < n:
#     print("*", end="")
#     i += 1

# n = int(input("Укажите количество:"))
#
# while n > 0:
#     print("*", end="")
#     n -= 1

# n = int(input('Введите количество символов: '))
# print("*" * n)

# n = input("Введите целое число: ")
#
# while type(n) != int:
#     try:
#         n = int(n)
#     except ValueError:
#         print("Число не целое")
#         n = input("Введите целое число: ")
#
#
# if n % 2 == 0:
#     print("Четное")
# else:
#     print("Нечетное")

# i = 0
# while i < 10:
#     if i == 3:
#         i += 1
#         continue
#     print(i, end=" ")
#     if i == 5:
#         break
#     i += 1
# print("\nЦикл завершен")

# while True:
#     n = int(input("Введите положительное число: "))
#     if n > 0:
#         break

# p = 1
# while True:
#     n = int(input("Введите число: "))
#     if n == 0:
#         break
#     p *= n
# print("Результат:", p)

# i = 0
# while i < 10:
#     if i == 5:
#         break
#     print(i)
#     i += 1
# else:
#     print("Цикл окончен i =", i)

# i = 1
# while i <= 9:
#     j = 1
#     while j <= 9:
#         print(i, "*", j, "=", j * i, end="\t\t")
#         j += 1
#     print()
#     i += 1

# i = 0
# while i < 3:
#     j = 0
#     while j < 6:
#         print('^', end='')
#         j += 1
#     print()
#     i += 1
#
# i = 1
# while i <= 5:
#     j = 0
#     while j < 20:
#         if i % 2 != 0:
#             print('+', end='')
#         else:
#             print('-', end='')
#         j += 1
#     print()
#     i += 1

# for element in collection:
#     print(element)

# for i in 'Hello!':
#     print(i)

# for color in "red", "orange", "yellow":
#     print("color", color)

# for i in range(n):
#     тело цикла
# range(start, stop, step)

# for i in range(2, 9, 3):
#     print(i, end=" ")
#
# print()
# j = 2
# while j < 9:
#     print(j, end=" ")
#     j += 3

# for i in range(100, 0, -10):
#     print(i, end=" ")

# a = int(input("Введите число: "))
# for i in range(1, a):
#     if a % i == 0:
#         print(i, end=" ")

# for i in range(10, 100):
#     if i % 11 == 0:
#         print(i, end=" ")
# print()
# for i in range(10, 100):
#     if i // 10 == i % 10:
#         print(i, end=" ")

# for i in range(3):
#     print(i)
#     if i == 1:
#         break
# else:
#     print("done")

# for i in range(3):
#     print("+++")
#     for j in range(2):
#         print("---")

# n = int(input('введите длину '))
# m = int(input('введите высоту '))
# for i in range(m):
#     for j in range(n):
#         print('*', end='')
#     print()

# a = int(input("высота прямоугольника"))
# b = int(input("Ширина прямоугольника"))
# for i in range(a):
#     print()
#     for j in range(b):
#         if 0 < i < a - 1 and 0 < j < b - 1:
#             print(" ", end="")
#         else:
#             print("*", end="")
# a = int(input("высота прямоугольника "))
# b = int(input("Ширина прямоугольника "))
# for i in range(a):  # СТРОКА
#     for j in range(b):  # СТОЛБЕЦ
#         if i == 0 or j == 0 or i == a - 1 or j == b - 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

# a = [letter * 2 for letter in "Hello"]
# print(a)
#
# for i in "Hello":
#     print(i * 2, end=",")

# num = [i for i in range(30) if i % 2 == 0]
# print(num)

#### Списки

# num = [8, 3, 9, 4, 1, "one", [1, 2, 3]]
# # print(num)
# # print(type(num))
# # print(num[6][1])
# # print(num[-1][1])
# # print(num[-2])
# # num[5] = 256
# # print(num)
# # num[1] += 100
# # print(num)
#
# print("Длина списка:", len(num))

# s = []
# print(type(s))
# b = list("Hello")
# print(b)

# s = [5, 1] * 6
# print(s)

# n = list(range(2, 10, 2))
# print(n)
# n2 = [2, 4, 6, 8]
# print(n2)
# if n == n2:
#     print("Равны")
# else:
#     print("Разные")

#### [выражение for переменная in последовательность]
# n = 5
# a = [i ** 2 for i in range(1, n + 1)]
# print(a)

# a = [1, 2, 3]
# b = [5, 6]
# c = a + b
# print(c)
# d = c * 2
# print(d)

# a = [0] * int(input("Введите количество элементов списка: "))
# print(a)
# for i in range(len(a)):
#     a[i] = int(input("-> "))
# print(a)

# a = [int(input("-> ")) for i in range(int(input("Количество элементов: ")))]
# print(a)
# a = [4, 8, 9, 3, 2]
# for i in range(len(a)):  # i - индексы
#     print(a[i], end=" ")
# print()
# for elem in a:  # i - элементы
#     print(elem, end=" ")

# lst = ["один", "два", "три"]
# for elem in lst:
#     print(elem, end=" ")
# print()
# for i in range(len(lst)):
#     print(lst[i], end=" ")
# s = 0
# a = [int(input("-> ")) for i in range(int(input("Количество элементов: ")))]
# for elem in a:
#     if elem < 0:
#         s += elem
# print(s)

# n = list(range(21, 41))
# print("Список:", n)
# k = s = 0
# for i in range(len(n)):
#     if n[i] % 2 == 0:
#         k += 1
#     else:
#         s += n[i]
# print("Количество четных:", k)
# print("Сумма нечетных:", s)

# n = [int(input("-> ")) for i in range(int(input("n= ")))]
# s = count = 0
# for i in n:
#     if i > 0:
#         s += i
#         count += 1
# print("Среднее:", s/count)

# n = [int(input("-> ")) for i in range(int(input("n= ")))]
# for i in range(len(n)):
#     if n[i] % 2 == 0:
#         print(i, end=" ")

# a = [int(input("-> ")) for i in range(int(input("n= ")))]
# for i in range(0, len(a), 2):
#     print(a[i], end=" ")

# a = [7, 8, 2, 1, 17]
# print(a)
# a[0], a[-1] = a[-1], a[0]
# print(a)

# size = int(input("Введите размер поля: "))
# symbol = int(input("Введите количество символов: "))
# for i in range(size):
#     for j in range(symbol):
#         for n in range(size):
#             for m in range(symbol):
#                 print(" " if (i + n) % 2 else "*", end="")
#         print()

# Срезы
# список[start:stop:step]
# s = [5, 9, 3, 7, 1, 8]
# print(s[1:4])
# print(s[1:])
# print(s[:2])
# print(s[::2])
# print(s[1::2])
# print(s[::-1])
# print(s[-2:2:-1])

# s = list(range(1, 8))
# print(s)
# print(s[:])
# print(s[::-1])
# print(s[::2])
# print(s[1::2])
# print(s[0:1:])
# print(s[-1::])
# print(s[3:4:])
# print(s[4::])
# print(s[-3:1:-1])
# print(s[2:5:])

# s = list(range(1, 8))
# print(s[:])
# s[1:3] = [0, 0, 0, 0]
# print(s)
# s[1:2] = [20]
# print(s)
# s[3] = 30
# print(s)

# Методы списков
# s = [1, 20, 0, 30, 4, 5, 6, 7]
# print(s)
# s.append(99)  # добавляет элемент в конец списка
# print(s)
# s.extend([9, 8, 7])  # добавляет множество элементов в конец списка
# print(s)
# s.extend("addd")
# print(s)
# s.insert(1, 100)  # добавляет заданное значение (второй параметр) по указанному индексу (первый параметр)
# print(s)

# s = []
# for i in range(1, 11):
#     s.extend([i ** 2])
# print(s)

# lst = []
# n = int(input("Введите количество элементов списка: "))
# for num in range(n):
#     x = int(input("Введите число: "))
#     # lst.append(x)
#     # lst.extend([x])
#     lst.insert(0, x)
# print(lst)

# lst = []
# n = int(input("Введите количество элементов списка: "))
# for num in range(n):
#     x = int(input("Введите число кратное 3: "))
#     if x % 3 == 0:
#         lst.append(x)
#     else:
#         print("Не делится")
# print(lst)

# a = [5, 9, 2, 1, 4, 3, 2, 4]
# b = [4, 2, 1, 3, 7]
# c = []
# for i in a:
#     for j in b:
#         if i in c:
#             continue
#         if i == j:
#             c.append(i)
#             break
# print(c)

# a = [1, 2, 3]
# b = [11, 22, 33, 4, 2]
# c = []
# if len(b) > len(a):
#     for i in range(len(a)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(a), len(b)):  # range(3,5)
#         c.append(b[i])
# print(a)
# print(b)
# print(c)
# a = [1, 2, 3, 4, 2]
# b = [11, 22, 33]
# c = []
# if len(b) > len(a):
#     for i in range(len(a)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(a), len(b)):  # range(3,5)
#         c.append(b[i])
# else:
#     for i in range(len(b)):
#         c.append(b[i])
#         c.append(a[i])
#     for i in range(len(b), len(a)):
#         c.append(a[i])
# print(a)
# print(b)
# print(c)

# s = [1, 20, 0, 30, 4, 5, 6, 7, 0, 2]
# # s[4:] = []
# # s[2:6] =[]
# # if 20 in s:
# s.remove(0)  # Удаляет значение (только первый найденный)
# print(s)
# last = s.pop()  # удаляет последний элемент из списка и возвращает удаляемый элемент
# print(last)
# print(s)
# second = s.pop(0)  # удаляет элемент по индексу
# print(s)
# # s.clear()  # очищает список
# del s[2]
# print(s)

# a = [int(input("-> ")) for i in range(int(input("n= ")))]
# print(a)
# k = int(input("Введите индекс: "))
# # del a[k]
# a.pop(k)
# print(a)


# print(dir(list))
# s = [1, 20, 0, 30, 4, 0, 5, 6, 7, 0, 2]
# num = s.count(5)  # считает количество заданных значений в списке
# print(num)
#
# ind = s.index(0, 3)  # возвращает положение первого индекса
# print(ind)

# a = [1, 2, 3]
# b = a
# s_copy = a.copy()  # возвращает копию списка, расположенную по-другому адресу
# print("a =", a)
# print("b =", b)
# print("s_copy =", s_copy)
# a.append(20)
# b.append(4)
# s_copy.append(444)
# print("a =", a)
# print("b =", b)
# print("s_copy =", s_copy)
# print(id(a))
# print(id(b))
# print(id(s_copy))

# s = [1, 20, 0, 30, 4, 0, 5, 6, 7, 0, 2]
# s.reverse()
# print(s)
# s.sort(reverse=True)  # используется для сортировки по убыванию reverse=True
# print(s)
#
# s2 = ["Виталий", "Сергей", "Александр", "Анна"]
# s2.sort(key=len)
# print(s2)
# srt = sorted(s)
# print(srt)
# print(s)

#### Генерация случайных данных

# import random
# print(random.randint(0, 9))
# print(random.random())

# from random import *
#
# print(randint(0, 9))  # от 0 по 9 включительно
# print(randrange(0, 10, 2))
# print(round(uniform(10.5, 25.5), 2))
#
# s = [55, 66, 77, 88, 99, 20, 30, 80, 90]
# print(choice(s))
# print(choices(s, k=3))
# shuffle(s)
# print(s)
#
# mas = [randint(0, 100) for i in range(10)]
# print(mas)

# lst = [5, 3, 2, 4, 1]
# print(len(lst))
# print(sum(lst))
# print(min(lst))
# print(max(lst))

# from random import *
# lst = [randint(0, 100) for i in range(10)]
# max_ = max(lst)
# print(lst)
# print(max_)
# lst.remove(max_)
# lst.insert(0, max_)
# print(lst)

# from random import *
# lst = [randint(-20, 20) for i in range(10)]
# print(lst)
# lst.sort(reverse=True)
# print(lst)

# from random import *
# lst = [randint(0, 100) for i in range(10)]
# print(lst)
# min_ = min(lst)
# print(min_)
# ind = lst.index(min_)
# print(ind)
# del lst[:ind]
# print(lst)

# x = list("1a2b3c4d")
# print(x)
# print("a" in x)
# print("e" in x)
# print("a" not in x)
# print("e" not in x)

# lst = []
# # if len(lst) == 0:
# print(bool(lst))
# if not lst:
#     print("Список пуст")
#
# from random import *
# n1 = int(input("Введите размер первого списка: "))
# n2 = int(input("Введите размер второго списка: "))
# a = [randint(0, 10) for i in range(n1)]
# b = [randint(0, 10) for j in range(n2)]
# print("Первый список: ", a)
# print("Второй список: ", b)
# c = a + b
# print("Третий список: ", c)
# c = []
# for i in range(len(a)):
#     if a[i] not in c:
#         c.append(a[i])
# for i in range(len(b)):
#     if b[i] not in c:
#         c.append(b[i])
# print("Элементы обоих списков без повторений: ", c)
# c = []
# for i in range(len(a)):
#     if a[i] in b and a[i] not in c:
#         c.append(a[i])
# print("Элементы общие для двух списков: ", c)
# c = [min(a), min(b), max(a), max(b)]
# print(c)

# from random import *
# k = int(input("размер списка "))
# s = []
# while len(s) < k:
#     n = randint(1, k)
#     if n not in s:
#         s.append(n)
# print(s)

# m = [
#     [1, 2, 3, 4, 5],  # строка 0
#     [5, 6, 7, 8],  # строка 1
#     [9, 10, 11, 12, 7, 8]  # строка 2
# ]
# print(m)
# print(m[1][2])

# for row in range(len(m)):
#     # print(m[row])
#     for col in range(len(m[row])):
#         print(m[row][col], end="\t")
#     print()

# for row in m:
#     # print(row)
#     for x in row:
#         print(x, end="\t")
#     print()

# m = [
#     [1, 2, 3, 4],  # строка 0
#     [5, 6, 7, 8],  # строка 1
#     [9, 10, 11, 12]  # строка 2
# ]
#
# for row in m:
#     for x in row:
#         print(x, end="\t")
#     print()
# print()
#
# q = [[x ** 2 for x in row] for row in m]
#
# for row in q:
#     for x in row:
#         print(x, end="\t")
#     print()

# n, m = int(input('Введите высоту матрицы: ')), int(input('Введите ширину матрицы: '))
# matr = [[0 for i in range(m)] for j in range(n)]
# for row in matr:
#     for x in row:
#         print(x, end='\t')
#     print()

# for x, y in [[1, 2], [3, 4], [5, 6], [7, 8]]:
#     print(x, "+", y, "=", x + y)

# from random import *
# w, h = 5, 4
# matrix = [[randint(1, 30) for x in range(w)] for y in range(h)]
# for row in matrix:
#     for x in row:
#         print(x, end='\t')
#     print()

# from random import *
# w, h = 3, 4
# matrix = [[randint(-20, 10) for i in range(w)] for j in range(h)]
# count = 0
# for row in matrix:
#     for x in row:
#         if x <0:
#             count +=1
#         print(x, end='\t')
#     print()
# print('Количество отрицательных элементов: ', count)

# from random import *
# w, h = 3, 4
# matrix = [[randint(0, 4) for i in range(w)] for j in range(h)]
# count = 1
# for row in matrix:
#     for x in row:
#         if x > 0:
#             count *= x
#         print(x, end='\t')
#     print()
# print('Произведение: ', count)


# w, h = 6, 6  # int(input("Число значений в строке"))
# matrix = [[random.randint(0, 10) for i in range(w)] for j in range(h)]
# print(matrix)
# for i in range (0,6,2):
#     print(i)
#     matrix[i],matrix[i+1]=matrix[i+1],matrix[i]
# print(matrix)

#
# from random import *
# w, h = 6, 6
# matrix = [[randint(0, 10) for i in range(w)] for j in range(h)]
# for row in matrix:
#     for x in row:
#         print(x, end='\t')
#     print()
# print()
#
# for row in range(len(matrix)):
#     if row % 2 == 0:
#         for col in range(len(matrix[row])):
#             print(matrix[row+1][col], end="\t")
#         print()
#         for col in range(len(matrix[row])):
#             print(matrix[row][col], end="\t")
#         print()

# import math
# print(dir(math))
# num1 = math.sqrt(2)
# print(num1)
# num2 = math.ceil(3.2)  # Округляет число вверх
# print(num2)
# num3 = math.floor(3.8)  # Округляет число вниз
# print(num3)
# print(math.pi)
#
# radius = 2
# print("Площадь окружности с радиусом:", radius, "=>", math.pi * (radius ** 2))

# import math
# rad = int(input("Введите радиус: "))
# print(round(2 * math.pi * rad, 2))

# import time
# second = time.time()
# print("Секунды сначала эпохи:", second)
# localtime = time.ctime()
# print(localtime)
# res = time.localtime()
# print(res)
# print(res.tm_year)
# print(time.strftime("Today is %B %d, %Y"))
# print(time.strftime("%m/%d/%Y, %H:%M:%S"))
#
# pause = 5
# print("Программа запустилась")
# time.sleep(pause)
# print(pause, "seconds")

# import time
# text = input("Название напоминания: ")
# local_time = float(input("Через сколько минут: "))
# local_time = local_time * 60
# time.sleep(local_time)
# print(text)


# start = time.monotonic()
# time.sleep(5)
# finish = time.monotonic()
# res = finish - start
# print(res)

# import locale
# locale.setlocale(locale.LC_ALL, 'ru')
# print(time.strftime("Сегодня: %B %d, %Y"))

# def hello(name, word):
#     print("Hello,", name, "Say", word)
#
#
# hello("Ирина", "hi")
# hello("Иван", "no")

# def get_sum(a, b):
#     print(a + b)
#
#
# x = 2
# y = 5
# get_sum(x, y)
# n = 7
# m = 9
# get_sum(n, m)

# def symbol(count, a, b):
#     for i in range(count):
#         if i % 2 != 0:
#             print(a, end="")
#         else:
#             print(b, end="")
#
#
# symbol(9, "+", "-")
# print()
# symbol(7, "X", "0")

# def get_sum(a, b):
#     return a + b
#
#
# x = 2
# y = 5
# res = get_sum(x, y)
# print(res)
# print(get_sum(1, 8))

# def maximum(one, two):
#     if one > two:
#         return one
#     else:
#         return two
#
#
# print(maximum(9, 6))

# def maximum(x, y):
#     if x > y:
#         return x - y
#     else:
#         return x + y
#
#
# a = int(input("a = "))
# b = int(input("b = "))
# print("Результат: ", maximum(a, b))


# def change(lst):
#     # lst[0], lst[-1] = lst[-1], lst[0]
#     start = lst.pop()
#     end = lst.pop(0)
#     lst.append(end)
#     lst.insert(0, start)
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change(["с", "л", "о", "н"]))

# def is_greater(x, y):
#     if x > y:
#         return True
#     else:
#         return False
#
#
# print(is_greater(10, 5))
#
# def check_password(password):
#     has_upper = False
#     has_lower = False
#     has_num = False
#
#     for ch in password:
#         if "A" <= ch <= "Z":
#             has_upper = True
#         elif "a" <= ch <= "z":
#             has_lower = True
#         elif "0" <= ch <= "9":
#             has_num = True
#
#     if len(password) >= 8 and has_upper and has_lower and has_num:
#         return True
#     return False
#
#
# p = input("Введите пароль: ")
# if check_password(p):
#     print("Надежный")
# else:
#     print("Ненадежный")

# def get_sum(a, b, c=0, d=1):
#     return a + b + c + d
#
#
# print(get_sum(1, 5, 2))
# q = 2
# print(get_sum(1, 5, d=q))

# def sym(a=20, b="-"):
#     return a * b
#
#
# print(sym(5, "*"))

# def digit_sum(n, even=True):
#     s = 0
#     while n > 0:
#         cur_digital = n % 10
#         if even and cur_digital % 2 == 0:
#             s += cur_digital
#         elif not even and cur_digital % 2:
#             s += cur_digital
#         n //= 10
#     return s
#
#
# print("Сумма четных цифр:")
# print(digit_sum(9874023))
# print(digit_sum(38271))
# print(digit_sum(123456789))
# print("Сумма нечетных цифр:")
# print(digit_sum(9874023, even=False))
# print(digit_sum(38271, even=False))
# print(digit_sum(123456789, even=False))

# def display_info(name, age):
#     print("Name:", name, "\nAge:", age)
#
#
# display_info("Ira", 23)
# display_info(23, "Ira")
# display_info(age=23, name="Ira")

# lt1 = [1, 2, 3]
# lt2 = [1, 2, 3]
# print(id(lt1))
# print(id(lt2))
# print(lt1 == lt2)
# print(lt1 is lt2)

# a = "hello"
# b = "hello"
# print(a == b)
# print(a is b)

# lt1 = [1, 2, 3]
# print(id(lt1))
# lt1.append(4)
# print(lt1)
# lt1.pop(1)
# print(lt1)
# lt1[1] = "Hello"
# print(lt1)
# print(id(lt1[1]))
# print(id(lt1))

# s = "Hello"
# print(id(s))
# s += "World"
# print(s)
# print(id(s))

# a = 5
# print(id(a))
# a += 1
# print(a)
# print(id(a))

# s = "Hello"
# print(id(s))
# s = s[1:-1]
# print(s)
# print(id(s))

# lt1 = [1, 2, 3]
# print(id(lt1))
# # lt1 = lt1[1:-1]
# lt1 = lt1 + [4, 5]
# print(lt1)
# print(id(lt1))

### Кортеж (tuple)
# lst = [10, 20, 30]
# tpl = (10, 20, 30)
# print(type(tpl))
# print(lst.__sizeof__())
# print(tpl.__sizeof__())
# a = (1, 2, 3, 4, 5)
# print(type(a))
# print(a)
# b = tuple()
# print(type(b))
# c = tuple("Hello")
# print(c)

# t = (1,)
# print(t)
# print(type(t))

# b = tuple((1, 2, 3, 4, 5))
# print(b)
# print(b[3])
# print(b[1:3])

# s = tuple(int(input("->" )) for i in range(3))
# print(s)

# s = input("Строка: ")
# a = tuple(s)
# print(a)
# from random import *
# mas = [randint(0, 100) for i in range(10)]
# print(mas)
# tpl = tuple(mas)
# print(tpl)
#
# print(tuple(randint(0, 100) for _ in range(10)))

# print(tuple(2 ** i for i in range(1, 13)))

# t1 = tuple("hello")
# t2 = tuple("world")
# t3 = t1 + t2
# print(t3)
# print(len(t3))
# print(t3.count("l"))
# print(t3.index("l"))
# print(t3.index("l", 4))
#
# for i in t3:
#     print(i, end=" ")

# from random import *
#
#
# def ran(a, b):
#     return tuple(randint(a, b) for _ in range(10))
#
#
# tpl1 = ran(0, 6)
# tpl2 = ran(-5, 1)
# print(tpl1)
# print(tpl2)
# tpl3 = tpl1 + tpl2
# print(tpl3)
# print('0 =', tpl3.count(0))

# t = (10, 11, [1, 2, 3], (4, 5, 6), ["hello", "world"])
# print(t, id(t))
# t[-1][0] = "new"
# t[4].append("hi")
# print(t, id(t))

# def create_tuple(lst):
#     s = []
#     for i in lst[::-1]:
#         if i not in s:
#             s.append(i)
#     return tuple(s)
# print(create_tuple([1, 2, 3, 3, 2]))
# print(create_tuple([2, 1, 3, 1, 2, 5, 5, 9, 2, 0, 0]))


# def tup(a_):
#     s = []
#     for i in a_:
#         if i not in s:
#             s.append(i)
#     return tuple(reversed(s))
#
#
# print(tup([1, 2, 3, 3, 2, 2]))

# t = (1, 2, 3)
# x = t[0]
# y = t[1]
# z = t[2]
# x, y, z = t
# print(x, y, z)


# def get_user():
#     name = "Tom"
#     age = 22
#     is_married = False
#     return name, age, is_married
#
#
# user = get_user()
# print(user)
# print(user[0])
# name1, age1, is_married1 = user
# print(name1)


# a = (1, 2, 3)
# # del a
# print(a)
# lst = list(a)
# lst.append(4)
# print(lst)
# tpl = tuple(lst)
# print(tpl)

# countries = (
#     ("Германия", 80.2, (("Берлин", 3.3), ("Гамбург", 1.718))),
#     ("Франция", 66, (("Париж", 2.2), ("Марсель", 1.6)))
# )
# print(countries, end="\n\n")
#
# for country in countries:
#     # print(country)
#     countryName, countryPopulation, cities = country
#     print("\nСтрана:", countryName, "население = ", countryPopulation)
#     for city in cities:
#         # print(city)
#         cityName, cityPopulation = city
#         print(cityName, cityPopulation)
#

#### Множество (set)

# s = {"banana", "apple", "orange", "apple"}
# print(type(s))
# print(s)
# print(len(s))
# c = ['hello', "world"]
# a = set(c)
# print(type(a))
# print(a)

# s = {x * x for x in range(10)}
# print(s)

# num = [1, 2, 2, 2, 3, 3, 4, 4, 5, 6]
# # num = set(num)
# # print(num)
# # num = list(num)
# num = list(set(num))
# print(num)

# def to_set(element):
#     element = set(element)
#     return element, len(element)
#
#
# print(to_set("я обычная строка"))
# print(to_set([4, 5, 4, 6, 2, 9, 11, 3, 4, 2]))

# t = {"red", "green", "blue"}
# # print("green" in t)
# for i in t:
#     print(i)

# r = ["ab_1", "ac_2", "bc_1", "bc_2"]
# # a = {i for i in r if "a" not in i}
# # a = {"A" + i[1:] if i[0] == 'a' else "B" + i[1:] for i in r}
# a = {"A" + i[1:] if i[0] == 'a' else "B" + i[1:] for i in r if i[1] == "c"}
# print(a)
#
# for i in r:
#     if i[1] == "c":
#         if i[0] == 'a':
#             print("A" + i[1:])
#         else:
#             print("B" + i[1:])

# a = {0, 1, 2, 3}
# a.add(4)
# print(a)

# a = {"Tom", "Bob", "Alice"}
# a.add("Ann")
# print(a)
# # a.remove("Tom")
# # print(a)
# # a.discard("Bob")
# # print(a)
# a.pop()
# print(a)

# a = {0, 1, 2, 3}
# b = {4, 3, 2, 1}
# # c = a.union(b)
# # c = a | b
# # print(c)
# # a.update(b)
# # a |= b
# # c = a & b
# # print(a)
# # print(c)
# # a &= b
# # print(a)
# # c = a - b
# c = a ^ b
# print(c)

# s1 = {1, 2}
# s2 = {3}
# s3 = {4, 5}
# s4 = {3, 2, 6}
# s5 = {6}
# s6 = {7, 8}
# s7 = {8, 9}
#
# s = s1.union(s2, s3, s4, s5, s6, s7)
# print(s)
# print(len(s))
# print(min(s))
# print(max(s))

# s1 = "Hello"
# s2 = "How are you"
# s = set(s1) & set(s2)
# print(s)

# s1 = "Python"
# s2 = "Programming language"
# s = set(s1) - set(s2)
# print(s)

# drawing = {"Марина", "Женя", "Света"}
# music = {"Костя", "Женя", "Илья"}
# only = drawing ^ music
# print("Одно хобби:", only)
# both = drawing & music
# print("Два кружка:", both)
# drawing = drawing - both
# print(drawing)

# s = frozenset([1, 2, 3, 4, 5])
# print(s)
# a = frozenset({"hello", "world"})
# print(a)

#### Словари

# s = ["one", "two"]
# print(s[0])
# d = {"1": "one", 2: "two", 3: "one"}
# print(d["1"])

# d = {"one": 1, "two": 2}
# print(d)
# print(type(d))
# d1 = dict(one=1, two=2)
# print(d1)
# print(type(d1))

# a = [
#     ("igor@gmail.com", "igor"),
#     ("irina@gmail.com", "irina"),
#     ("anna@gmail.com", "anna")
# ]
# d = dict(a)
# print(d)
#
# d = {a: a ** 2 for a in range(7)}
# print(d[2])
# d[2] = 15
# print(d)
# d[6] = 4 ** 2
# print(d)

# d = {0: "text", "one": 45, (1, 2.3): "кортеж", 42: [2, 3, 6, 7], True: 1}
# print(d)
# print(d[True])
# print(d[(1, 2.3)])
# print(d[42][1])
# print("one" in d)
# print("two" in d)
# print(d.keys())

# if "one" in d:
#     print("TRUE")
#

# key = (1, 2.3)

# if key in d:
#     del d[key]

# try:
#     del d[key]
# except KeyError:
#     print("Элемента с ключом" + str(key) + "нет в словаре")
#
# print(d)

# d = {0: "text", "one": 45, (1, 2.3): "кортеж", 42: [2, 3, 6, 7], True: 1}
# print(d)
#
# for key in d:
#     print(key, d[key])

# d = {"x1": 3, "x2": 7, "x3": 5, "x4": -1}
# p = 1
# for key in d:
#     p *= d[key]
# print(p)

# d = dict()
# d[1] = input("-> ")
# d[2] = input("-> ")
# d[3] = input("-> ")
# d[4] = input("-> ")
# print(d)

# d = dict()
# for i in range(1, 5):
#     d[i] = input('->')
# print(d)

# d = {a: input('-> ') for a in range(1, 5)}
# a = int(input('Какой элемент исключить? '))
# if a in d:
#     del d[a]
#     print(d)
# else:
#     print('Такого элемента нет')

# capitals = dict()
# capitals["Россия"] = "Москва"
# capitals["Италия"] = "Рим"
# capitals["Испания"] = "Мадрид"
#
# countries = ["Россия", "Италия", "Франция", "Испания"]
#
# for country in countries:
#     if country in capitals:
#         print("Столица страны " + country + ":" + capitals[country])
#     else:
#         print("В базе нет страны", country)
#
# goods = {
#     "1": ["Core-i3-4330", 9, 4500],
#     "2": ["Core-i5-4670K", 3, 8500],
#     "3": ["AMD FX-6300", 6, 3700],
#     "4": ["Pentium 63220", 8, 2100],
#     "5": ["Core-i5-3450", 5, 6400]
# }
#
# for i in goods:
#     print(i, ") ", goods[i][0], " - ", goods[i][1], " шт. по ", goods[i][2], "руб.", sep="")
#
# while True:
#     n = input("N: ")
#     if n != "0":
#         cnt = int(input("Количество: "))
#         goods[n][1] = cnt
#     else:
#         break
#
# for i in goods:
#     print(i, ") ", goods[i][0], " - ", goods[i][1], " шт. по ", goods[i][2], "руб.", sep="")

# goods = {
#     "1": {"a": "Core-i3-4330", "b": 9, "c": 4500}
# }
# print(goods["1"]["a"])

# d = {"a": 1, "b": 2, "c": 3}
# print(d["b"])
# value = d.get("e", "No")
# print(value)
# print(d)
# item = d.items()
# print(item)
# key = d.keys()
# print(key)
# value = d.values()
# print(value)
#
# for i, j in d.items():
#     print(i, "->", j)

# d.clear()
# print(d)
# item = d.pop("b")
# print(item)
# it = d.popitem()
# print(it)
# item = d.setdefault("e", 5)
#
# print(item)
# d.update([("a", 7), ("q", 9)])
# print(d)

# d = {"a": 1, "b": 2, "c": 3}
# d2 = d.copy()
# print("d =", d)
# print("d2 =", d2)
# d["e"] = 7
# print("d =", d)
# print("d2 =", d2)

# x = {"a": 1, "b": 2}
# y = {"b": 3, "c": 4}
# # c = x.copy()
# # c.update(y)
# c = x | y
# print(c)

# d1 = {'name': 'Kelly', 'age':25 , 'salary': 8000, 'city': 'New York'}
# d2 = {}
# name = d1.pop('name')
# salary = d1.pop('salary')
# print(d1)
# d2['name'] = name
# d2['salary'] = salary
# print(d2)

# d = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New York"}
# new = dict()
# new["name"] = d.pop("name")
# new["salary"] = d.pop("salary")
# print(d)
# print(new)

# d = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New York"}
# print(d)
# d["location"] = d.pop("city")
# print(d)
#
# a = {
#     "First": {
#         1: "one",
#         2: "two",
#         3: "three"
#     },
#     "Second": {
#         4: "four",
#         5: "five"
#     }
# }
# print(a)
# for x in a:
#     print(x)
#     for y in a[x]:
#         print(y)

# d = {"один": 1, "два": 2, "три": 3, "четыре": 4}
# # a = {value: key for key, value in d.items()}
# a = {value: key for key, value in d.items() if value <= 2}
# print(a)

# value = int(input("->"))
# lt = [1, 2, 3, 4, 5]
# a = {i: value for i in lt}
# print(a)

# d = dict.fromkeys(["a", "b"], 100)
# print(d)

# value = int(input("-> "))
# a = {i: value for i in range(1, 9)}
# print(a)

# figures = {1: "Rectangle", 2: "Triangle", 3: "Circle"}
# value = list(figures.items())
# print(value)

# a = ["one", 1, 2, 3, "two", 10, 20, "three", 15, 36, 60, "four", -20]
# d = dict()
# s = None
#
# for i in a:
#     if type(i) == str:
#         d[i] = []
#         s = i
#     else:
#         d[s].append(i)
# print(d)

# zip()

# d = dict(zip([12, 1, 2], ["Dec", "Jan", "Feb"]))
# print(d)

# a = [12, 1, 2]
# b = ["dec", "jan", "feb"]
# f = {k: v for k, v in zip(a,b)}
# print(f)

# print(list(zip(range(5), range(100))))

# a = {"name": "Igor", "last_name": "Doe", "job": "consultant"}
# b = {"name": "Irina", "last_name": "Smith", "job": "manager"}
# c = {"name": "Irina", "last_name": "Smith", "job": "manager"}
#
# for (k1, v1), (k2, v2), (k3, v3) in zip(a.items(), b.items(), c.items()):
#     print(k1, "-> ", v1, ", ", v2, ", ", v3, sep="")
#     # print(k2, "-> ", v2)
#     # print(k3, "-> ", v3)

# a = [(1, "a"), (2, "b"), (3, "c"), (4, "d")]
# x, y = zip(*a)
# print(x)
# print(y)

# lt1 = [2, 1, 4, 3]
# lt2 = ["d", "a", "c", "b"]
# # a1 = list(zip(lt1, lt2))
# # print(a1)
# # a1.sort()
# a = sorted(zip(lt2, lt1))
# print(a)

# month = ["January", "February", "March"]
# total_sales = [52000.00, 51000.00, 48000.00]
# prod_cost = [46800.00, 45900.00, 43200.00]
#
# for sales, cost, m in zip(total_sales, prod_cost, month):
#     res = sales - cost
#     print("Чистая прибыль в", m, "=", res)

# one = {"apple": 0.4, "orange": 0.35, "banana": 0.6}
# two = {"pepper": 0.2, "onion": 0.55}
# print({**one, **two})
#
# for k, v in {**one, **two}.items():
#     print(k, "->", v)


# en = ["red", "green", "blue"]
# j = 1
# for i in en:
#     print(j, "-й цвет: ", i, sep="")
#     j += 1

# en = ["red", "green", "blue"]
#
# for j, i in enumerate(en, 1):
#     print(j, "-й цвет: ", i, sep="")

# en = {0: 1, 1: 2, 2: 3}
#
# for i, j in enumerate(en):
#     print(i, ": ", j,"->", en[j], sep="")

# a = [1, 2, 3]
# b = [*a, 4, 5, 6]
# print(b)


# def func(*args):
#     return args
#
#
# print(func(1))
# print(func(1, 2, 3, "abc"))
# print(func())

# def summa(*params):
#     res = 0
#     for i in params:
#         res += i
#     return params
#
#
# num1 = summa(1, 2, 3, 4, 5, 6, 7, 8)
# num2 = summa(6, 7, 8)
# print(num1)
# print(num2)

# def to_dict(*args):
#     dic = {}
#     for i in args:
#         dic[i] = i
#     return dic
#
#
# print(to_dict(1, 2, 3, 4))
# print(to_dict("gray", (2, 17), 3.11, -4))


# def func(*num):
#     lst = []
#     a = sum(num) / len(num)
#     print(a)
#     for i in num:
#         if i < a:
#             lst.append(i)
#     return lst
#
#
# print(func(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(func(3, 6, 1, 9, 5))

# def func(a, *args):
#     return a, args
#
#
# print(func(1))
# print(func(1, 2, 3, "abc"))

# def print_scores(student, *scores):
#     print("Student name:", student)
#     for score in scores:
#         print(score, end=" ")
#     print()
#
#
# print_scores("John", 100, 95, 88, 92, 99)
# print_scores("Rick", 96, 20, 33)


# def func(*args):
#     res = []
#     for i in args:
#         res.append(int(str(i)[::-1]))
#     return res
#
#
# print(func(12, 2345, 323, 4456, 5687, 62, 734, 81, 91))

# def reverse_num(n):
#     s = str(n)
#     return int(s[::-1])
#
#
# def func(*args, only_odd=False):
#     res = []
#     for i in args:
#         if not only_odd or (only_odd and i % 2 != 0):
#             res.append(reverse_num(i))
#     return res
#
#
# print(func(12, 2345, 323, 4456, 5687, 62, 734, 81, 91))
# print(func(12, 2345, 323, 4456, 5687, 62, 734, 81, 91, only_odd=True))

# def func(**kwargs):
#     return kwargs
#
#
# print(func(a=1, b=2, c=3))
# print(func())
# print(func(a="Python"))


# def info(**data):
#     for k, v in data.items():
#         print(k, "->", v)
#     print()
#
#
# info(first_name="Irina", last_name="Petrova", age=22, phone=1234567890)
# info(first_name="Igor", last_name="Ivanov", age=36, email="igor@gmail.com", country="Russia", phone=1234567890)

# def db(**kwargs):
#     my_dict.update(kwargs)
#
#
# my_dict = {"one": "first"}
# db(k1=22, k2=31, k3=11, k4=91)
# db(name="Bob", age=31, weight=61, eyes_color="gray")
# print("My_dict = ", my_dict)

# def func1(*args):
#     print(args[0])
#
#
# def func2(**kwargs):
#     print(kwargs["one"])
#
#
# func1(1, 2, 3, 4, 5)
# func2(one=123, two=456)

# def func(a, *args, one=True, **kwargs):
#     return a, args, kwargs, one
#
#
# print(func(5, 9, 7, 8, 6, one=False, b=2, c=3, d=4))

# Область видимости (scope)

# for i in range(5):
#     a = 5
#     print(i)
#
# print("i за пределами цикла", i)
# print("a за пределами цикла", a)

# if True:
#     a = 5
# print("a =", a)

# name = "Tom"
#
#
# def hi():
#     print("Hello", name)
#
#
# def bye():
#     global name
#     name = "Bob"
#     print("Good bye", name)
#
#
# hi()
# bye()
# print(name)

# i = 5
#
#
# def func(arg=i):
#     print(arg)
#
#
# i = 6
# func()  # 5


# def add_two(a):
#     x = 2
#     return a + x
#
#
# print(add_two(3))


# def func(a):
#     x = 2
#
#     def inner():
#         print("x=", x)
#         return a + x
#
#     return inner()
#
#
# print(func(5))

# import builtins
#
# print(dir(builtins))

# Вложенные функции

# def outer_func(who):
#     def inner_func():
#         print("Hello", who)
#     inner_func()
#
#
# outer_func("world!")

# def func1():
#     a = 6  # отрабатывает 2 строка
#
#     def func2(b):
#         a = 4  # отрабатывает 5 строка
#         print("Сумма: ", a + b)
#
#     print("a:", a)  # отрабатывает 3 строка
#     func2(4)  # отрабатывает 4 строка
#
#
# func1()  # отрабатывает 1 строка

# x = 25
# t = 0
#
#
# def fn():
#     global t
#     a = 30
#     print("global:", x)  # 25
#
#     def inner():
#         nonlocal a
#         a = 35
#         print("nonlocal:", a)  # 35
#
#     inner()
#     print(a)
#     t = a
#
#
# fn()
# z = x + t  # 25 + 30
# print("res:", z)

# x = 5
#
#
# def fn1():
#     x = 25
#
#     def fn2():
#         # x = 33
#
#         def fn3():
#             nonlocal x
#             x = 55
#
#         fn3()
#         print("fn2.x=", x)
#
#     fn2()
#     print("fn1.x=", x)
#
#
# fn1()
# print("x=", x)
#
# def outer(a1, b1, a2, b2):
#     a = 0
#     b = 0
#
#     def inner():
#         nonlocal a, b
#
#         a = a1 + a2
#         b = b1 + b2
#
#     inner()
#     return [a, b]
#
#
# res = outer(2, 3, -1, 4)
# print(res)

# def increment(number):
#     def inner():
#         return number + 1
#     return inner()
#
#
# print(increment(10))

# Замыкание

# def outer(n):
#     def inner(x):
#         return n + x
#     return inner
#
#
# # res = outer(5)
# # print(res(10))
# # print(res(2))
# # res2 = outer(7)
# # print(res2(5))
#
# print(outer(5)(10))

# def func1():
#     a = 1
#     b = "line"
#     c = [1, 2, 3]
#
#     def func2():
#         nonlocal a, b
#         c.append(4)
#         a = a + 1
#         b = b + "_new"
#         return a, b, c
#
#     return func2
#
#
# func = func1()
# print(func())

# def func(city):
#     s = 0
#
#     def inner():
#         nonlocal s
#         s += 1
#         print(city, s)
#
#     return inner
#
#
# res1 = func("Москва")
# res1()
# res1()
# res2 = func("Сочи")
# res2()
# res2()
# res1()

# students = {
#     "Alice": 100,
#     "Bob": 67,
#     "Chris": 85,
#     "David": 75,
#     "Elise": 54,
#     "Fiona": 35,
#     "Grace": 69
# }
#
#
# def make_classifier(lower, upper):
#     def classify_student(exam):
#         return {k: v for k, v in exam.items() if lower <= v < upper}
#
#     return classify_student
#
#
# A = make_classifier(80, 101)
# B = make_classifier(70, 80)
# C = make_classifier(50, 70)
# D = make_classifier(0, 50)
# print(A(students))
# print(B(students))
# print(C(students))
# print(D(students))

# def func(a, b):
#     def add():
#         return a + b
#
#     def sub():
#         return a - b
#
#     def mul():
#         return a * b
#
#     def replace():
#         pass
#
#     replace.add = add
#     replace.sub = sub
#     replace.mul = mul
#     return replace
#
#
# obj1 = func(5, 2)
# print(obj1.add())
#
# obj2 = func(5, 2)
# print(obj2.sub())
#
# obj3 = func(5, 2)
# print(obj3.mul())


# Анонимные функции, лямбда - выражения

# print((lambda x, y: x + y)(1, 2))
# (lambda x, y: print(x + y))(1, 2)
# print((lambda x, y: x + y)("a", "b"))
#
# func = lambda x, y: x + y
# print(func(1, 2))
# print(func("a", "b"))

# print((lambda x, y: x ** 2 + y ** 2)(2, 5))

# summ = lambda a=1, b=2, c=3: a + b + c
#
# print(summ())
# print(summ(10))
# print(summ(10, 20))

# func1 = lambda *args: args
#
# print(func1(1, 2, 3, 4))

# c = (lambda x: x * 2,
#      lambda x: x * 3,
#      lambda x: x * 4)
#
# for t in c:
#     print(t("abc_"))
#
# def inc(n):
#     return lambda x: x + n
#
#
# f = inc(42)
# print(f(3))
#
#
# def inc1(n):
#     def wrap(x):
#         return x + n
#
#     return wrap
#
#
# f1 = inc1(42)
# print(f1(3))
#
# inc2 = (lambda n: (lambda x: x + n))
# # f2 = inc2(42)
# # print(f2(3))
# print(inc2(42)(3))
#
# print((lambda n: (lambda x: x + n))(42)(3))

# print((lambda a: (lambda b: (lambda c: a + b + c)))(2)(4)(6))


# d = {"b": 15, "a": 10, "c": 4}
# lst = list(d.items())
# print(lst)
# lst.sort(key=lambda i: i[1])
# print(lst)
# dict1 = dict(lst)
# print(dict1)

# players = [
#     {'name': 'Антон', 'last name': 'Бирюков', 'raiting': 9},
#     {'name': 'Алексей', 'last name': 'Бодня', 'raiting': 10},
#     {'name': 'Федор', 'last name': 'Сидоров', 'raiting': 4},
#     {'name': 'Михаил', 'last name': 'Семенов', 'raiting': 6}
# ]
#
# res = sorted(players, key=lambda item: item["last name"])
# print(res)
# res = sorted(players, key=lambda item: item["raiting"])
# print(res)
# res = sorted(players, key=lambda item: item["raiting"], reverse=True)
# print(res)

# a = [(lambda x, y: x + y), (lambda x, y: x - y), (lambda x, y: x * y), (lambda x, y: x / y)]
# b = a[0](12, 5)
# print(b)

# a = {"one": lambda x: x-1, "two": lambda x: abs(x) - 1, "three": lambda x: x}
# b = [-3, 10, 0, 2]
# for i in b:
#     if i < 0:
#         print(a["two"](i))
#     elif i > 0:
#         print(a["one"](i))
#     else:
#         print(a["three"](i))

# d = {
#     1: (lambda: print("Понедельник")),
#     2: (lambda: print("Вторник")),
#     3: (lambda: print("Среда")),
#     4: (lambda: print("Четверг")),
#     5: (lambda: print("Пятница")),
#     6: (lambda: print("Суббота")),
#     7: (lambda: print("Воскресенье")),
# }
#
# d[4]()

# maximum = (lambda a, b: a if a > b else b)
# print(maximum(15, 23))

# minimun = (lambda a, b, c: a if a < b else b if b < c else c)
# print(minimun(9, 8, 5))

# Функция map()

# def multiple(t):
#     return t * 2


# lst = [2, 8, 12, -5, -10]

# print(list(map(multiple, lst)))
# print(list(map(lambda t: t * 2, lst)))
# print(list(map(lambda i: i * 2, range(2, 10))))

# t = (2.88, -7.75, 100.55)
# print(tuple(map(lambda x: str(x), t)))
#
# a = ['2.88', '-7.75', '100.55']
# print(list(map(float, a)))

# areas = [3.578945, 5.1234567, 7.456789, 56.4123658, 9.0123456, 32.7789456]
# print(list(map(round, areas, range(1, 7))))

# st = ["a", "b", "c", "d", "e"]
# num = [1, 2, 3, 4, 5]
#
# lst = dict(map(lambda x, y: (x, y), st, num))
# print(lst)

# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
#
# lst = list(map(lambda x, y: x + y, l1, l2))
# print(lst)

# filter(func, iterable)

# t = ("abcd", "abc", "cdefq", "def", "ghi")
# t2 = tuple(filter(lambda s: len(s) == 3, t))
# print(t2)

# b = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
# res = list(filter(lambda s: s > 75, b))
# print(res)

# from random import *
#
# lst = [randint(1, 40) for i in range(10)]
# print(lst)
# res = list(filter(lambda s: 10 <= s <= 20, lst))
# print(res)

# lst = [45, 55, 60, 37, 100, 105, 220]
# res = list(filter(lambda x: x % 15 == 0, lst))
# print(res)

# Декораторы

# def hello():
#     return "Hello, I am func hello"
#
#
# def super_func(func):
#     print("Hello, I am func super_func")
#     print(func())
#
#
# super_func(hello)

# def my_decorator(func):
#     def wrap():
#         print("Code before")
#         func()
#         print("Code after")
#
#     return wrap
#
#
# def func_test():
#     print("Hello")
#
#
# test = my_decorator(func_test)
# test()

# def my_decorator(func):  # декорирующая функция
#     def wrap():
#         print("Code before")
#         func()
#         print("Code after")
#
#     return wrap
#
#
# @my_decorator  # декоратор
# def func_test():  # декорируемая функция
#     print("Hello")
#
#
# func_test()
#
# def bold(fn):
#     def wrap():
#         return "<b>" + fn() + "/b"
#
#     return wrap
#
#
# def italic(fn):
#     def wrap():
#         return "<i>" + fn() + "/i"
#
#     return wrap
#
#
# @italic
# @bold
# def hello():
#     return "text"
#
#
# print(hello())
#
# def cnt(fn):
#     count = 0
#
#     def wrap():
#         nonlocal count
#         count += 1
#         fn()
#         print("Вызов функции: ", count)
#     return wrap
#
#
# @cnt
# def hello():
#     print("hello")
#
#
# hello()
# hello()

# def args_decorator(fn):
#     def wrap(arg1, arg2):
#         print("*" * 50)
#         fn(arg1, arg2)
#         print("*" * 50)
#
#     return wrap
#
#
# @args_decorator
# def print_full_name(first, last):
#     print("Меня зовут", first, last)
#
#
# print_full_name("Ирина", "Лаврова")

# def args_decorator(fn):
#     def wrap(*args, **kwargs):
#         fn(*args, **kwargs)
#         print("*" * 50)
#         print("args:", args)
#         print("kwargs:", kwargs)
#         print("*" * 50)
#
#     return wrap
#
#
# @args_decorator
# def print_full_name(a, b, c, study="Python"):
#     print(a, b, c, "изучают", study)
#
#
# print_full_name("Ирина", "Борис", "Светлана", study="JS")
# print()
# print_full_name("Владимир", "Екатерина", "Виктор")

# def decor(args1, args2):
#     def args_dec(fn):
#         def wrap(x, y):
#             print(args1, x, args2, y, "=", end=" ")
#             fn(x, y)
#         return wrap
#     return args_dec
#
#
# @decor("Сумма:", "+")
# def summa(a, b):
#     print(a + b)
#
#
# @decor("Разность:", "-")
# def sub(a, b):
#     print(a - b)
#
#
# summa(5, 2)
# sub(5, 2)

# def multiply(args):
#     def func(fn):
#         def wrap(x):
#             print("Результат:")
#             return fn(x) * args
#
#         return wrap
#     return func
#
#
# @multiply(3)
# def return_num(num):
#     return num
#
#
# print(return_num(5))

# def typed(*args, **kwargs):
#     def wrapper(fn):
#         def wrap(*f_args, **f_kwargs):
#             for i in range(len(args)):
#                 if type(f_args[i]) != args[i]:
#                     raise TypeError("Некорректный тип данных")
#             for k in kwargs:
#                 if type(f_kwargs[k]) != kwargs[k]:
#                     raise TypeError("Некорректный тип данных")
#             return fn(*f_args, **f_kwargs)
#         return wrap
#     return wrapper
#
#
# @typed(int, int, int)
# def typed_fn(x, y, z):
#     return x * y * z
#
#
# @typed(str, str, str)
# def typed_fn2(x, y, z):
#     return x + y + z
#
#
# @typed(str, str, z=int)
# def typed_fn3(x, y, z="Hello!"):
#     return (x + y) * z
#
#
# print(typed_fn(3, 4, 5))
# # print(typed_fn(3, 4, "Doge"))
# print(typed_fn2("Hello,", "World", "!"))
# print(typed_fn3("Hello,", "World", z=5))

# def decor(tx=None, decor_text=""):
#     def wrapper(fn):
#         def wrap(*args):
#             print(decor_text, end=" ")
#             fn(*args)
#
#         return wrap
#     if tx is None:
#         return wrapper
#     else:
#         return wrapper(tx)
#
#
# @decor
# def hello_world2(text):
#     print(text)
#
#
# @decor(decor_text="Hello,")
# def hello_world(text):
#     print(text)
#
#
# hello_world2("Hi!")
# hello_world("world!")

# print(int("100", 2))
# print(int("100", 8))
# print(int("100", 16))
# print(int("100", 10))

# print(bin(18))  # 0b10010
# print(oct(18))  # 0o22
# print(hex(18))  # 0x12
# print(0b100 + 2)
# print(0o20)
# print(0x17)

# q = "Pyt"
# w = "hon"
# e = q + w
# print(e)
# # print(e * 3)
# # print("y" in e)
# # print(e[1])
# # print(e[::-1])
# e = e[:3] + "t" + e[4:]
# print(e)

# def change_char(s, c_old, c_new):
#     s2 = ""
#     for i in s:
#         if i != c_old:
#             s2 += i
#         else:
#             s2 += c_new
#
#     return s2
#
#
# st = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования."
# st2 = change_char(st, "N", "P")
# print("st1 =", st)
# print("st2 =", st2)

# print(u"Привет")
# print(r"C:\file.txt")  # r - "сырые" строки - игнорирует спец. символы
# print("C:\\file.txt")
# print(r"C:\file.txt\\"[:-1])
# print(r"C:\file.txt" + "\\")
# print("C:\\file.txt\\")

# name = "Дмитрий"
# age = 25
# print("Меня зовут " + name + ". Мне " + str(age) + " лет.")
# print("Меня зовут ", name, ". Мне ", age, " лет.", sep="")
# print(f"Меня зовут {name}. Мне {age} лет")
#
# print(f"{round(2.356789, 2)}")
# print(f"{2.356789:.2f}")

# x = 10
# y = 5
# print(f"{x} x {y} / 2 = {x * y / 2}")

# d = 74
# print(f"{{{d}}}")

# dir_name = "doc"
# file_name = "data.txt"
# print(fr"home\{dir_name}\{file_name}")
# print("home\\" + dir_name + "\\" + file_name)

# s = """ <div>
#     <a href="#">content</a>
# </div>
# """
# print(s)


# def square(n):
#     """Принимает число n, возвращает квадрат числа n"""
#     return n ** 2
#
#
# print(square(5))
# print(square.__doc__)


# import math
#
#
# def cylinder(r, h):
#     """
#     Вычисляет площадь цилиндра.
#
#     Вычисляет площадь цилиндра на основании заданной высоты и радиуса основания.
#
#     :param r: положительное число, радиус основания цилиндра.
#     :param h: положительное число, высота цилиндра.
#     :return: положительное число, площадь цилиндра.
#     """
#     return 2 * math.pi * r * (r + h)
#
#
# print(cylinder(2, 4))
# print(cylinder.__doc__)

# print(ord("a"))
#
# while True:
#     n = input("-> ")
#     if n != "-1":
#         print(ord(n))
#     else:
#         break

# my_str = "Test string for me"
# arr = [ord(x) for x in my_str]
# print(arr)
# arr = [int(sum(arr) / len(arr))] + arr
# print(arr)
# arr += [x for x in [ord(x) for x in (input("-> "))[0:6:2]] if x not in arr]  # вводится с пробелами
# print(arr)
# if arr[-1] in arr[:-1]:
#     print(arr.count(arr[-1]) - 1)
# arr.sort(reverse=True)
# print(arr)

# print(chr(97))
# print(chr(35))

# a = 122
# b = 97
#
# while b < a+1:
#     print(chr(b), end=" ")
#     b += 1

# a = 122
# b = 97
# if a > b:
#     for i in range(b, a+1):
#         print(chr(i), end=' ')
# else:
#     for i in range(a, b+1):
#         print(chr(i), end=' ')

# print("apple" == "Apple")
# print("apple" > "Apple")
# print(ord("a"))
# print(ord("A"))

# from random import randint
#
# SHORTEST = 7
# LONGEST = 10
# MIN_ASCII = 33
# MAX_ASCII = 126
#
#
# def random_password():
#     random_length = randint(SHORTEST, LONGEST)
#     res = ""
#     for i in range(random_length):
#         random_char = chr(randint(MIN_ASCII, MAX_ASCII))
#         res += random_char
#     return res
#
#
# print("Ваш случайный пароль:", random_password())

# print(dir(str))

# s = "hello, WORLD! I am learning Python."
# print(s.capitalize())  # Hello, world! i am learn python.
# print(s.lower())  # hello, world! i am learn python.
# print(s.upper())  # HELLO, WORLD! I AM LEARN PYTHON.
# print(s.swapcase())  # HELLO, world! i AM LEARN pYTHON.
# print(s.title())  # Hello, World! I Am Learn Python.
#
# print(s.count("l", 3))
# print(s.find("Pyth"))  # ищет в строке заданную подстроку, если найдена, то возвращает индекс первого найденного,
# # если нет, то -1

# a = "один два"
# b = a[:a.find(" ")]
# c = a[a.find(" ") + 1:]
# print(c + " " + b)

# a = "ab12c59p7dq"
# digits = []

# for i in a:
#     if i in "1234567890":
#         digits.append(int(i))
# print(digits)

# for i in a:
#     if "1234567890".find(i) != -1:
#         digits.append(int(i))
# print(digits)

# s = "hello, WORLD! I am learning Python."
# print(s)
# print(s.index("Python"))  # ищет в строке заданную подстроку, если найдена, то возвращает индекс первого найденного,
# # если нет, то будет исключение

# print(s.rfind("h"))

# s = "I am learning Python. hello, WORLD! "
# a1 = s.find("h")
# a2 = s.rfind("h")
# s = s[:a1] + s[a2+1:]
# print(s)

# print("abc123".isalnum())  # определяет состоит ли строка из цифр и (или) букв
# print("ABCabc".isalpha())  # определяет состоит ли строка из букв
# print("123".isdigit())  # определяет состоит ли строка из цифр
# print("abc".islower())  # определяет состоит ли строка из строчных букв
# print("ABC".isupper())  # определяет состоит ли строка из заглавных букв

# print("py".center(30, '*'))

# print("    py".lstrip())  # удаляет пробелы с левой стороны
# print("py    ".rstrip())  # удаляет пробелы с правой стороны
# print("    py".strip())  # удаляет пробелы слева и справа
#
# print("https://www.python.org".lstrip("/:pths"))
# print("py.$$$;".rstrip(";$."))
#
# print("https://www.python.org".lstrip("htps:/").rstrip("org."))

# st = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования."
# print(st)
# print(st.replace("Nython", "Python", 2))  # заменяет вхождение подстроки в строке

# s = "-"
# seq = ("a", "b", "c")
# print(s.join(seq))
#
# print("..".join(["1", "2"]))  # объединяет итерируемою последовательность (список, кортеж, другая строка) в одну
# # строку через заданный символ разделитель
# print(":".join("Hello"))

# print("Строка разделенная пробелами".split())  # делит строку на список из подстрок
# # print("Строка разделенная пробелам_и".split("_"))
# # print("Строка разделенная пробелами".split("а"))
#
# print("www.python.org.ru".split(".", 2))

# a = list(map(int, input("-> ").split()))
# print(a)

# a = input('Введите ФИО: ').split()
# print(a)
# print(a[0], ' ', a[1][0], '.', a[2][0], '.', sep='')

# print("www.python.org.ru.".split("."))
# print("www.python.org.ru.".split(".", 2))
# print("www.python.org.ru.".rsplit(".", 2))
#
# print("www...python...org".split("."))

# s = "В строке заменить пробелы символом"
# print(s)
# s = s.split(" ")
# print(s)
# s = "*".join(s)
# print(s)

# import re

# s = "Я ищу совпадения в 2023 году. И я их найду в 2 счёта."
# reg = r"\."

# print(re.findall(reg, s))  # ['я', 'я'] возвращает список, содержащий все совпадения
# print(re.findall("12", s))  # []
#
# print(re.search(reg, s))  # находит местоположение первого совпадения объекта
# print(re.search(reg, s).span())
# print(re.search(reg, s).start())
# print(re.search(reg, s).end())
# print(re.search(reg, s).group())

# print(re.match(reg, s))  # поиск по заданному шаблону в начале строки

# print(re.split(reg, s, 1))  # возвращает список, в котором строка разбита по шаблону

# print(re.sub(reg, "!", s))  # заменяет совпадения указанным текстом

# import re
#
# s = "Я ищу совпадения в 2023 году. И я их найду в 2 счёта. 9578"
# # reg = r"[12][09][0-9][0-9]"
# # reg = r"[А-Яа-яё]"  # [А-Яа-яЁё]
# reg = r"[А-яё.]"  # [А-Яа-яЁё]
#
# print(re.findall(reg, s))
#
# s1 = "Ели[-ели]."
# pattern = r"[А-яё.-\[\]]"
# print(re.findall(pattern, s1))

# import re

# s1 = "Час в 24-часовом формате от 00 до 23. 2021-06-15Т21:45. Минуты в диапазоне от 00 до 59. 2021-06-15Т01:09."
# pattern = "[0-2][0-9]:[0-5][0-9]"
# print(re.findall(pattern, s1))

# s = "Я ищу совпадения в 2023 году. И я их найду в 2 счёта. 9578 19_45"
# reg = r"\W"
# print(re.findall(reg, s))

import re


# s = "Я ищу совпадения в 2023 году. И я их найду в 2 счёта. 9578 19_4 5"
# reg = r"20*"

# print(re.findall(reg, s))

# Повторения
# "+" - от 1 до бесконечности
# "*" - от 0 до бесконечности (2023, 2 = ['20', '2', '2'], двойка обязательна, а ноль может быть или не быть)
# "?" - 0 или 1

# s1 = "Цифры: 7, +17, -42, 0013, 0.3564"
# # pattern = r"[+-]?\d+[.\d]*"
# pattern = r"[+-]?\d+\.?\d*"
# print(re.findall(pattern, s1))

# s1 = "05-03-1987 # Дата рождения"
# print(re.sub(r"#.*", "", s1))
#
# print("Дата рождения:", re.sub(r"-", ".", re.sub(r"#.*", "", s1)))

# s1 = "author=Пушкин А.С.; title  = Евгений Онегин; price =200; year= 1831"
# pattern = r"\w+\s*=\s*[^;]+"
# print(re.findall(pattern, s1))

# s1 = "12 сентября 2021 года"
# reg1 = r"\d{2}"
# print(re.findall(reg1, s1))

# s = "+7 499 456-45-78, +74994564578, 7 (499) 456 45 78, 74994564578"
# reg1 = r"\+?7\d{10}"
# print(re.findall(reg1, s))

# s = "Я ищу совпадения в 2023 году. И я их найду в 2 счёта. 9578 19_4 5"
# # reg = r"^\w+\s\w+"
# reg = r"\w+\s\w+$"
#
# print(re.findall(reg, s))


# def login(a):
#     return re.findall(r"^[\w!@#$-]{8,25}$", a)
#
#
# print(login("admin_admin"))
# print(login("admin_admin@"))

# print(re.findall(r"\w+", "12 + й"))
# print(re.findall(r"\w+", "12 + й", flags=re.ASCII))

# print(re.findall(r"[а-я]", "Я я", re.IGNORECASE))

# text = """
# one
# two
# """
# print(re.findall(r"one$", text))
# print(re.findall(r"one$", text, re.MULTILINE))

# text = """
# one
# two
# """
#
# print(re.findall(r"one.\w+", text, re.DOTALL))

# print(re.findall("""
# [A-z.-]+  # part 1
# @  # поиск символа @
# [a-z_.-]+  # part 2
# """, "test@mail.ru", re.VERBOSE))

# text = "hello world"
# print(re.findall(r"\w\+", text, re.DEBUG))

# text = """Python,
# python,
# PYTHON
# """
# reg = "(?im)^python"
# print(re.findall(reg, text))  # flags=re.IGNORECASE | re.MULTILINE

# s = "123456@i.ru, 123_456@ru.name.ru, login@i.ru, логин-1@i.ru, login.3@i.ru, login.3-67@i.ru, 1login@ru.name.ru"
# reg = r"[\w.-]+@[\w.]+\w{2,3}"
# print(re.findall(reg, s))

# text = "<body>Пример жадного соответствия регулярных выражений</body>"
# print(re.findall("<.+?>", text))

# greedy (жадный)
# lazy (ленивый)

# *?, +?, ??
# {m,n}?, {,n}?, {m,}?

# t = "2324 786 22 4569"
# reg = r"\d{1,3}?"
# print(re.findall(reg, t))

# s = "<p>Изображение <img alt='картинка' src='bg.jpg' title='подсказка'> - фон страницы</p>"
# reg = r"<img\s+[^>]*src\s*=\s*[^>]+>"
# reg = r"<img[^>]*>"
# reg = r"<img.*?>"
# print(re.findall(reg, s))

# s = "Python (в русском языке встречаются названия питон[16] или пайтон[17]) - высокоуровненый язык программирования " \
#     "общего назначения с динамической строгой типизацией и автоматическим управлением памятью[18][19]."
# reg = r"\[\d+\]"
# print(re.findall(reg, s))

# s = "Петр и Ольга отлично учатся!"
# reg = "Петр|Виталий|Ольга"
# print(re.findall(reg, s))

# s = "int = 4, float = 45.0, double = 8.0f"
# reg = r"(?:int|double)\s*=\s*\d+[.\w+]*"
# # reg = r"int\s*=\s*\d+[.\w+]*|double\s*=\s*\d+[.\w+]*"
# print(re.findall(reg, s))

# () - группирующая скобка
# (?:) - группирующая скобка, не сохраняющая

# s = "127.0.0.1"
# reg = r"(?:\d{1,3}.){3}\d{1,3}"
# # reg = r"\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}"
# print(re.findall(reg, s))

# s = "Word2016, PS6, AI5"
# reg = r"(([A-z]+)(\d*))"
# print(re.findall(reg, s))

# s = "5 + 7*2 - 4"
# # reg = r"\s*([+*-])\s*"  # ['5', '+', '7', '*', '2', '-', '4']
# # reg = r"\s*[+*-]\s*" ['5', '7', '2', '4']
# print(re.split(reg, s))

# s = "Я ищу совпадения в 2023 году. И я их найду в 2 счёта."
# reg = r"([0-9]+)\s(\D+)"
# print(re.search(reg, s).group())
# m = re.search(reg, s)
# print(m[1])
# print(m[2])
# print(m[0])


# text = """
# Самара
# Москва
# Тверь
# Уфа
# Казань
# """
# count = 0
#
#
# def replace_find(m):
#     global count
#     count += 1
#     return f"<option value='{count}'>{m.group(1)}</option>\n"
#
#
# print(re.sub(r"\s*(\w+)\s*", replace_find, text))

# s = "<p>Изображение <img src='bg.jpg'> - фон страницы</p>"
# reg = r"<img\s+[^>]*src=([\"'])(.+)\1>"
# print(re.findall(reg, s))

# s = "<p>Изображение <img src='bg.jpg'> - фон страницы</p>"
# reg = r"<img\s+[^>]*src=(?P<q>[\"'])(.+)(?P=q)>"
# print(re.findall(reg, s))

# s = "Самолет прилетает 10/23/2023. Будем рады вас видеть после 10/24/2023."
# reg = r"(\d{2})/(\d{2})/(\d{4})"
# print(re.findall(reg, s))
# print(re.sub(reg, r"\2.\1", s))

# s = "google.com and google.ru"
# reg = r"(([a-z0-9-]{2,}\.)+[a-z]{2,4})"
# print(re.sub(reg, r"http://\1", s))

# Рекурсия

# def elevator(n):
#     if n == 0:
#         print("Вы в подвале")
#         return
#     print("=> ", n)
#     elevator(n - 1)
#     print(n, end=" ")
#
#
# n1 = int(input("На каком Вы этаже: "))
# elevator(n1)

# def sum_list(lst):
#     res = 0
#     for i in lst:
#         res += i
#     return res
#
#
# print(sum_list([1, 3, 5, 7, 9]))

# def sum_list(lst):
#     if len(lst) == 1:
#         print(lst, "=> lst[0]:", lst[0])
#         return lst[0]
#     else:
#         print(lst, "=> lst[0]:", lst[0])
#         return lst[0] + sum_list(lst[1:])
#
#
# print(sum_list([1, 3, 5, 7, 9]))


# def to_str(n, base):
#     convert = "0123456789ABCDEF"
#     if n < base:
#         return convert[n]
#     else:
#         return to_str(n // base, base) + convert[n % base]
#
#
# print(to_str(255, 16))

# names = ['Adam', ["Bob", ["Chet", "Cat"], "Bard", "Bert"], 'Alex', ["Bea", "Bill"], 'Ann']

# print(names[0])
# print(isinstance(names[0], list))
# print(names[1][1])
# print(isinstance(names[1][1], list))
# print(names[1][1][0])
# print(isinstance(names[1][1][0], list))


# def count(lst):
#     cnt = 0
#     for i in lst:
#         if isinstance(i, list):
#             cnt += count(i)
#         else:
#             cnt += 1
#     return cnt
#
#
# print(count(names))


# names = ['Adam', ["Bob", ["Chet", "Cat"], "Bard", "Bert"], 'Alex', ["Bea", "Bill"], 'Ann']
#
#
# def union(s):
#     if not s:  # s == [] - список пустой
#         return s
#     if isinstance(s[0], list):
#         return union(s[0]) + union(s[1:])
#     return s[:1] + union(s[1:])
#
#
# print("Выпрямленный список:", union(names))


# def remove(text):
#     if not text:
#         return ""
#     if text[0] == "\t" or text[0] == " ":
#         return remove(text[1:])
#     else:
#         return text[0] + remove(text[1:])
#
#
# print(remove("  Hello\tWorld  "))