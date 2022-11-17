def sr(fn):
    def wrap(*x):
        print("Сумма чисел", *x, "=", fn(*x))
        print("Среднее арифметическое чисел", *x, "=", end=" ")
        return fn(*x) / len(x)

    return wrap


@sr
def sum_(*args):
    return sum(args)


print(sum_(2, 3, 3, 4))
