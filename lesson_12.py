# Задание 1
###############################################

# d1 = {1: 10, 2: 20}
# d2 = {3: 30, 4: 40}
# d3 = {5: 50, 6: 60}
#
# d = {**d1, **d2, **d3}
# print(d)

###############################################
# Задание 2
###############################################
#
# d = {
#     "emp1": {
#         "name": "John",
#         "salary": 7500
#     },
#     "emp2": {
#         "name": "Emma",
#         "salary": 8000
#     },
#     "emp3": {
#         "name": "Brad",
#         "salary": 6500
#     }
# }
# print(d["emp3"])
# print(d["emp3"]["salary"])
# d["emp3"]["salary"] = 8500
#
# for i in d:
#     print(i)
#     for j in d[i]:
#         print(j, ":", d[i][j])

###############################################
# Задание 3
###############################################

# num = int(input("Количество студентов: "))
# l_name = []
# l_bal = []
# for i in range(1, num + 1):
#     print(i, end="")
#     name = input("-й студент: ")
#     l_name.append(name)
#     for j in l_name:
#         bal = int(input("Балл: "))
#         l_bal.append(bal)
#         break
#
# d = dict(zip(l_name, l_bal))
# print()
# sr_bal = 0
# for i in d.values():
#     sr_bal += i
# sr_bal = sr_bal / num
# print("Средний балл: ", sr_bal, ". Студенты с баллом выше среднего: ", sep="")
#
# for key, value in d.items():
#     if value >= sr_bal:
#         print(key)
