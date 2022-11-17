# Задание 1
###############################################

# m_1 = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
# m_2 = [
#     [0, 0, 0],
#     [0, 0, 0],
#     [0, 0, 0],
#     [0, 0, 0]
# ]
#
# for i in m_1:
#     for j in i:
#         print(j, end="\t\t")
#     print()
# print()
#
# for i in range(len(m_1)):
#     for j in range(len(m_1[0])):
#         m_2[j][i] = m_1[i][j]
#
# for i in m_2:
#     for j in i:
#         print(j, end="\t\t")
#     print()

###############################################
# Задание 2
###############################################

# from random import *
# h, w = 6, 6
# lst_1 = [[randint(0, 10) for y in range(w)] for i in range(h)]
# for i in lst_1:
#     for j in i:
#         print(j, end='\t')
#     print()
#
# lst_2 = [randint(0, 10) for i in range(h)]
# print(lst_2)
# print()
#
# for i in range(len(lst_1)):
#     if i % 2 != 0:
#         for j in range(len(lst_1[i])):
#             print(lst_1[i][j], end='\t')
#         print()
#     else:
#         for x in lst_2:
#             print(x, end='\t')
#         print()
#
#

