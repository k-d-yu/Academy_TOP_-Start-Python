# Задание 1
###############################################

read_file_1 = "one.txt"
read_file_2 = "two.txt"
write_file = "three.txt"

with open(read_file_1, "r") as r_f_1, open(read_file_2, "r") as r_f_2, open(write_file, "w") as w_f:
    for line_1 in r_f_1:
        for line_2 in r_f_2:
            w_f.write(line_1 + line_2)
            break

###############################################
# Задание 2
###############################################

import os

dirs = ["Work/F1", "Work/F2/F21"]

# for d in dirs:
#     os.makedirs(d)

files = {"Work": ["w.txt"],
         "Work/F1": ["f11.txt", "f12.txt", "f13.txt"],
         "Work/F2/F21": ["f211.txt", "f212.txt"]
         }

for d, file in files.items():
    for f in file:
        file_pass = os.path.join(d, f)
        open(file_pass, "w").close()

file_text = ["Work/w.txt", "Work/F1/f12.txt", "Work/F2/F21/f211.txt", "Work/F2/F21/f212.txt"]
for file in file_text:
    with open(file, "w") as f:
        f.write(f"Текст для файла по пути {file}.")

print("Обход Work снизу вверх")
for root, dirs, files in os.walk("Work", topdown=False):
    print(root)
    print(dirs)
    print(files)
print("-" * 30)

print("Обход Work сверху вниз")
for root, dirs, files in os.walk("Work"):
    print(root)
    print(dirs)
    print(files)
print("-" * 30)


