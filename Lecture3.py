# Print variables using different separators
a = 12
b = "asd"
f = 6.77
print(a, b, f, sep=", ")
print(a, b, f, sep="\n", end=", ")  # Next print will be in this same row
print(a, b, f, sep="")

# Slice of sequences
s = "Hi there!"
s1 = s[0:-3]  # Slice of s, from 0 index to -3
print(s1)
s2 = s[0:5:3]  # Slice of s, from indexes 0 to 5 with step 3
print(s2)
s3 = s[::-1]  # Reversed list
print(s3)
s4 = s[2:8:-1]
print(s4)
s5 = s[7:1:-1]  # Correct slicing of what we wanted preset previously^.
print(s5)  # If we want to use reverse step, we need to mark indexes assuming this.

# Тернарка
l0 = [1, 2, 3]
s = len(l0) if type(l0) is list else None

x = int(input("Enter number "))
x = "Good" if x % 2 == 0 else "Bad"
print(x)

# Удаление последнего элемента списка, пока он не будет пустым
l1 = [1, 2, 3]

while l1:  # Пока список не пустой он будет True
    print(l1.pop())
print(l1)

# range
for i in range(2, 10, 2):
    print(i)

# For
l2 = [1, 23, 13, 467, 50, 6]
for item in l2:
    if item % 2 == 0:
        print(item)
    else:
        print(item + 1)
print(l2)

# С изменением значений нечетных. Работа с индексами
l3 = [1, 23, 13, 467, 50, 6]
for i1 in range(len(l3)):
    # print("index", i)
    # print("value", l3[i])
    if l3[i1] % 2 == 1:
        l3[i1] += 1
print(l3)

# Break
while True:
    phrase = input("Enter a phrase without whitespaces ")
    if phrase.count(" ") == 0:
        print(phrase)
        break

# Variant 2 of ^
while True:
    phrase = input("Enter a phrase without whitespaces ")
    if " " not in phrase:
        print(phrase)
        break

# Variant 3 of ^ but without counting of spaces on start/end of phrase
while True:
    phrase = input("Enter a phrase without whitespaces ").strip()
    if " " not in phrase:
        print(phrase)
        break
