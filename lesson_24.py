# Задание 1
###############################################

# def func(lst):
#     count = 0
#     if not lst:
#         return count
#     if lst[0] >= 0:
#         return func(lst[1:])
#     else:
#         count += 1
#         return count + func(lst[1:])
#
#
# print(func([-2, 3, 8, -11, -4, 6]))

###############################################
# Задание 2
###############################################

lst = ['Adam', ["Bob", ["Chet", "Cat"], "Bard", "Bert"], 'Alex', ["Bea", "Bill"], 'Ann']

count = 0
for i in range(len(lst)):
    if isinstance(lst[i], list):
        for j in range(len(lst[i])):
            if isinstance(lst[i][j], list):
                for k in range(len(lst[i][j])):
                    count += 1
            else:
                count += 1
    else:
        count += 1

print(count)
