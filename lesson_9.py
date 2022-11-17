def slicer(tup_, num_):
    count = tup_.count(num_)
    if count == 0:
        return ()
    elif count > 1:
        index_1 = tup_.index(num_)
        index_2 = tup_.index(num_, index_1 + 1)
        return tup_[index_1:index_2 + 1]
    elif count == 1:
        index_1 = tup_.index(num_)
        return tup_[index_1:]


tup_1 = (1, 2, 3)
tup_2 = (1, 8, 3, 4, 8, 8, 9, 2)
tup_3 = (1, 2, 8, 5, 1, 2, 9)
num = 8
print((tup_1, num))
print((tup_2, num))
print((tup_3, num))
print()
print(slicer(tup_1, num))
print(slicer(tup_2, num))
print(slicer(tup_3, num))
