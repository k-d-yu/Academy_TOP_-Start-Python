# def smash(words):
#     return " ".join(map(str, words))
#
#
# print(smash(["hello", "world", 1]))

# def hoop_count(n):
#     if n >= 10:
#         return "Great, now move on to tricks"
#     else:
#         return "Keep at it until you get it"
#
#
# print(hoop_count(9))

# def digitize(n):
#     mas_1 = []
#     mas = list(str(n))
#     mas.reverse()
#     for i in mas:
#         mas_1.append(int(i))
#     return mas_1
#
#
# print(digitize(23582357))

# def find_smallest_int(arr):
#     return min(arr)
#
#
# print(find_smallest_int([34, 15, 88, 2]))
# print(find_smallest_int([34, -345, -1, 100]))

# def divisors(n):
#     k = 1
#     s = 0
#     while k <= n:
#         if n % k == 0:
#             s += 1
#         k += 1
#     return s
#
#
# print(divisors(12))

# def count_by(x, n):
#     lst = []
#     for x in range(x, (n * x) + 1, x):
#         lst.append(x)
#     return lst
#
#
# print(count_by(50, 5))

# def hero(bullets, dragons):
#     if dragons * 2 <= bullets:
#         return True
#     else:
#         return False
#
#
# print(hero(100, 40))

# def better_than_average(class_points, your_points):
#     return your_points >= sum(class_points) / len(class_points)
#
#
# print(better_than_average([12, 23, 34, 45, 56, 67, 78, 89, 90], 69))

# def no_space(x):
#     return x.replace(" ", "")
#
#
# print(no_space('8 j 8   mBliB8g  imjB8B8  jl  B'))

# def first_non_consecutive(arr):
#     i = 1
#     for x in arr:
#         if i < len(arr) and arr[i] - arr[i-1] != 1:
#             return arr[i]
#         i += 1
#     return None
#
#
# print(first_non_consecutive([1, 2, 3, 4, 6, 7, 8]))
# print(first_non_consecutive([1, 2, 3, 4, 5, 6, 7, 8]))
# print(first_non_consecutive([4, 6, 7, 8, 9, 11]))
# print(first_non_consecutive([4, 5, 6, 7, 8, 9, 11]))

# def count_sheeps(sheep):
#     count = 0
#     for i in sheep:
#         if i == True:
#             count += 1
#     return count
#
#
# print(count_sheeps([True, True, True, False,
#                     True, True, True, True,
#                     True, False, True, False,
#                     True, False, False, True,
#                     True, True, True, True,
#                     False, False, True, True]))


# def boolean_to_string(b):
#     return str(b)
#
#
# print(boolean_to_string(True))

# def sum_two_smallest_numbers(numbers):
#     min_1 = min(numbers)
#     numbers.remove(min_1)
#     min_2 = min(numbers)
#     return min_1 + min_2
#
#
# print(sum_two_smallest_numbers([5, 8, 12, 18, 22]))
# print(sum_two_smallest_numbers([7, 15, 12, 18, 22]))


# def filter_list(l):
#     lst = []
#     for i in l:
#         if type(i) == int:
#             lst.append(i)
#     return lst
#
#
# print(filter_list([1, 'a', 'b', 0, 15]))


# def high_and_low(numbers):
#
#
#
#
# print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))

# def correct(s):
#     s = list(s)
#     s_ = []
#     for i in s:
#         if i != "0" and i != "1" and i != "5":
#             s_.append(i)
#         elif i == "5":
#             s_.append("S")
#         elif i == "0":
#             s_.append("O")
#         elif i == "1":
#             s_.append("I")
#
#     return "".join(s_)
#
#
# print(correct("L0ND0N"))
# print(correct("51NGAP0RE"))

# def remove_exclamation_marks(s):
#     return s.replace("!", "")
#
#
# print(remove_exclamation_marks("Hello World!"))
# print(remove_exclamation_marks("Hello World!!!"))

# def square_sum(numbers):
#     s = 0
#     for i in numbers:
#         s += i ** 2
#     return s
#
#
# print(square_sum([1, 2]))
# print(square_sum([0, 3, 4, 5]))

# def solution(string):
#     return string[::-1]
#
#
# print(solution('world'))

# def open_or_senior(data):
#     lst = []
#     for i in data:
#         if i[0] >= 55 and i[1] > 7:
#             lst.append("Senior")
#         else:
#             lst.append("Open")
#     return lst
#
#
# print(open_or_senior([(45, 12), (55, 21), (19, -2), (104, 20)]))
# print(open_or_senior([(16, 23), (73, 1), (56, 20), (1, -1)]))

# def double_char(s):
#     lst = []
#     for i in s:
#         lst.append(i*2)
#     return "".join(lst)
#
#
# print(double_char("String"))
# print(double_char("1234!_ "))


# def find_short(s):
#     lst = []
#     s = s.split()
#     for i in s:
#         lst.append(len(i))
#     return min(lst)
#
#
# print(find_short("bitcoin take over the world maybe who knows perhaps"))
# print(find_short("Let's travel abroad shall we"))

# a = 8
# i = 0
# count = 0
#
# while i <= 22:
#     count += i
#     i += 1
# print(count)

# def summation(num):
#     i, count = 0, 0
#     while i <= num:
#         count += i
#         i += 1
#     return count
#
#
# print(summation(100))


# def invert(lst):
#     return [i * -1 for i in lst]


# def number(lines):
#     mas = []
#     count = 1
#     for i in range(len(lines)):
#         mas.append(str(count) + ": " + lines[i])
#         count += 1
#     return mas


# print(number(["a", "b", "c"]))

# a = [f"{i}: {j}" for i, j in enumerate(["a", "b", "c", "d"], 1)]

# import re
#
#
# def get_count(sentence):
#     return len(re.findall(r"[aeiou]", sentence,))
#
#
# print(get_count("aeyg"))

# import re
#
#
# def disemvowel(string_):
#     return "".join(re.findall(r"[^aeiou]", string_, re.IGNORECASE))
#
#
# print(disemvowel("This website is for losers LOL"))
