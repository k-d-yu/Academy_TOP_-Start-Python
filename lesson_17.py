def func(n):
    s = ""
    while n > 0:
        if n % 2 == 0:
            s += "0"
        else:
            s += "1"
        n = n // 2
    print(s[::-1])


print("Для выхода нажмите \"0\"")
while True:
    num = int(input("Введите число -> "))
    if num != 0:
        func(num)
    else:
        print("Выход из программы")
        break
