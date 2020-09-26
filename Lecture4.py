l = ("asdasdasd", "mbmnbmnbm", "asdd", "qweqweqweq", "cxzc")
s = 0
for item in l:
    if len(item) % 2 == 1:
        s += 1
print(s)

# Exceptions
# Raise
# name = "3lena"
# if name[0].isnumeric():
#     raise NameError("Invalid Name!")

# Assert
mass = int(input("Enter mass: "))
assert mass > 0, "Mass can't be less than 0"
print(mass)
