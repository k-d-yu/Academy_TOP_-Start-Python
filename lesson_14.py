# Задание 1
###############################################

# def func_compute(num):
#     def inner(a):
#         return a * num
#
#     return inner
#
#
# res = func_compute(2)
# print(res(15))
# print(res(20))
# res = func_compute(3)
# print(res(15))
# print(res(20))

###############################################
# Задание 2
###############################################

# Вариант 1 - Локальная переменная

# def func(a1, b1, c1):
#     s = 0
#
#     def inner():
#         nonlocal s
#         s = (a1 * b1) + (b1 * c1) + (a1 * c1)
#
#     inner()
#     return 2 * s
#
#
# print(func(2, 4, 6))
# print(func(5, 8, 2))
# print(func(1, 6, 8))

# Вариант 2 - Глобальная переменная

# s = 0
#
#
# def func(a1, b1, c1):
#     global s
#
#     def inner():
#         global s
#         s = (a1 * b1) + (b1 * c1) + (a1 * c1)
#
#     inner()
#     return 2 * s
#
#
# print(func(2, 4, 6))
# print(func(5, 8, 2))
# print(func(1, 6, 8))

# Вариант 3 - Нелокальная переменная

# def func(a1, b1, c1):
#     def inner():
#         s = (a1 * b1) + (b1 * c1) + (a1 * c1)
#         return 2 * s
#
#     return inner()
#
#
# print(func(2, 4, 6))
# print(func(5, 8, 2))
# print(func(1, 6, 8))
