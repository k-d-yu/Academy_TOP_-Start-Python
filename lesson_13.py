# Задание 1
###############################################

# def func(*args):
#     s = 1
#     for i in args:
#         s *= i
#     return s
#
#
# print(func(10, 9))
# print(func(2, 3, 4))
# print(func(3, 5, 10, 6))

###############################################
# Задание 2
###############################################

# def func(*args):
#     s = 0
#     lst = []
#     for i in args:
#         s += i
#         lst.append(s)
#     for i in lst:
#         print(i, end=" ")
#     print()
#
#
# func(3, 9, 1)
# func(2, 5, 4, 2)
# func(3, 5, 10, 6, 3)

###############################################
# Задание 3
###############################################

# import math
#
#
# def func(figure_type, **kwargs):
#     if figure_type == "rhombus":
#         return (kwargs["d1"] * kwargs["d2"]) / 2
#     elif figure_type == "square":
#         return kwargs["a"] ** 2
#     elif figure_type == "trapezoid":
#         return 0.5 * (kwargs["a"] + kwargs["b"]) * kwargs["h"]
#     elif figure_type == "circle":
#         return math.pi * kwargs["r"] ** 2
#     else:
#         return "No!"
#
#
# print(func(figure_type="rhombus", d1=10, d2=8))
# print(func(figure_type="square", a=5))
# print(func(figure_type="trapezoid", a=12, b=3, h=6))
# print(func(figure_type="circle", r=18))
# print(func(figure_type="unknown", a=1, b=2, c=3))
