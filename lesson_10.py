# Задание 1
###############################################

# def ch(num_):
#     lst = []
#     for i in num_:
#         if i % num == 0 and i > 0:
#             lst.append(i)
#     for j in lst:
#         return max(lst)
#     return "no such numbers"
#
#
# num = 13
# print(ch([2, 7, 0, 3, 1, 5, -13]))
# print(ch([2, 7, 0, 3, 1, 5, -13, 13]))
# print(ch([26]))
# print(ch([99, 99, 100, 34, -39]))
# print(ch([99, 39, 99, 100, 34]))

###############################################
# Задание 2
###############################################

# print("Введите элементы кортежа:")
# tp = tuple(input("-> ") for _ in range(5))
# s = input("Введите элемент для поиска: ")
# print("Исходный кортеж:", tp)
# print("S =", s)
# if s in tp:
#     print("Yes")
# else:
#     print("No")


###############################################
# Задание 3
###############################################

# print("Введите элементы кортежа:", end=" ")
# tp = input()
# tp = tuple(str(tp))
# print(tp)
# lst = []
# for i in tp:
#     if i not in lst:
#         lst.append(i)
#         print(i, "=", tp.count(i))

