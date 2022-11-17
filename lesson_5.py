lst = [0] * int(input("Введите элементы списка: \nn= "))
for i in range(len(lst)):
    lst[i] = int(input("-> "))

for i in range(len(lst)):
    if i == 0:
        continue
    elif lst[i - 1] < lst[i]:
        print(lst[i], end=" ")
