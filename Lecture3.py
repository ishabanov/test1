#Print variables using different separators
a = 12
b = "asd"
f = 6.77
print(a, b, f, sep = ", ")
print(a, b, f, sep = "\n", end = ", ") #Next print will be in this same row
print(a, b, f, sep = "")

#Slice of sequences
s = "Hi there!"
s1 = s[0:-3] #Slice of s, from 0 index to -3
print(s1)
s2 = s[0:5:3] # Slice of s, from indexes 0 to 5 with step 3
print(s2)
s3 = s[::-1] #Reversed list
print(s3)
s4 = s[2:8:-1]
print(s4)
s5 = s[7:1:-1] #Correct slicing of what we wanted preset previously^.
print(s5) #If we want to use reverse step, we need to mark indexes assuming this.

#Тернарка
l = [1, 2, 3]
s = len(l) if type(l) is list else None

x = int(input("Enter number "))
x = "Good" if x % 2 == 0 else "Bad"
print(x)

#Удаление последнего элемента списка, пока он не будет пустым
l = [1, 2, 3]

while l: #Пока список не пустой он будет True
    print(l.pop())    
print(l)

#range
for i in range(2, 10, 2):
    print(i)

#For
l = [1, 23, 13, 467, 50, 6]
for item in l:
    if item % 2 == 0:
        print(item)
    else:
        print(item + 1)
print(l)

#С изменением значений нечетных. Работа с индексами
l = [1, 23, 13, 467, 50, 6]
for i in range(len(l)):
    # print("index", i)
    # print("value", l[i])
    if l[i] % 2 == 1:
        l[i] += 1
print(l)

#Break
while True:
    phrase = input("Enter a phrase without whitespaces ")
    if phrase.count(" ") == 0
        print(phrase)
break