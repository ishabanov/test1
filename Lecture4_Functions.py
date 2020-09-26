# def repeat(s, exclaim):
#     result = s * 3
#     if exclaim:
#         return result + "!!!"
#     return result
#
#
# r = repeat("wow ", True)
# print(r)

# Hypotenuse function
def hyp(cat1, cat2):
    h = (cat1 ** 2 + cat2 ** 2) ** (1 / 2)
    return h


h1 = hyp(3, 4)
h2 = hyp(4, 4)
h3 = hyp(1, 2)
print(h1, h2, h3)


# Leave only letters inside the string (remove everything else)
def clean_str(s):
    l = list(s)
    for sym in s:
        if not sym.isalpha():
            l.remove(sym)
    res = "".join(l)  # обьединение списка обратно в строку с промежутком из пустой строки

    return res


z = clean_str("kfh432424nbbsjkbsdf/.,")
print(z)


# Выводим второе по возрастанию значение из аргументов, которых может быть сколько угодно
def penult(*args):
    n = list(args)
    n.sort()
    return n[1]


print(penult(2, 7, 5, 10, 555))


def named(**kwargs):
    return "{} is {}".format(kwargs.get("a"), kwargs.get("b"))


print(named(a=3))
