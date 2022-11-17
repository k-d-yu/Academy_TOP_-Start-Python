import re


def password(pas):
    return re.findall(r"^[\dA-z@_-]{6,18}$", pas)


# pass_ = "my_p@ssw0rd"
pass_ = input("-> ")
print(password(pass_))
