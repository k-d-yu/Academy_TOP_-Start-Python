f = open('text.txt', 'w')
f.write("Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;\n")
f.close()

f = open('text.txt', 'r')
f_read = f.readlines()
print(f_read)

pos1 = int(input("pos1 = "))
pos2 = int(input("pos2 = "))

if 0 <= pos1 < len(f_read) and 0 <= pos2 < len(f_read):
    if pos2 > pos1:
        f_read_copy = f_read.copy()
        p_1 = f_read.pop(pos1)
        p_2 = f_read_copy.pop(pos2)
        f_read.remove(p_2)
        f_read.insert(pos1, p_2)
        f_read.insert(pos2, p_1)
        print(f_read)
    elif pos2 < pos1:
        f_read_copy = f_read.copy()
        p_1 = f_read.pop(pos1)
        p_2 = f_read_copy.pop(pos2)
        f_read.remove(p_2)
        f_read.insert(pos2, p_1)
        f_read.insert(pos1, p_2)
        print(f_read)
    else:
        print("Одинаковые строки")
else:
    print("Такой строки нет")
f.close()

f = open("text.txt", "w")
f.writelines(f_read)
f.close()

