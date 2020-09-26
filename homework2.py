# Task_1

# 1. Определите является ли строка записью числа.
s1 = "-10"
print("1.", s1.isnumeric())

# 2. Посчитайте сколько у вас пробелов в строке.
s2 = "blah blah blah blah"
print("2.", s2.count(" "))

# 3. Посчитайте сколько у вас символов точки &#39;.&#39; в строке.
s3 = "asd.asd.asdddd.asd.qweee.qwee"
print("3.", s3.count("."))

# 4. Создайте строку &quot;Homework&quot;. Преобразуйте её в строку длиной 100 символов,
# посередине которой исходное слово, а с обоих сторон строка заполнена
# пробелами. Выведите её на экран. Убедитесь, что у вас 100 символов
# (посчитайте длину).
s4 = "{:^100}".format("Homework")
print("4.", s4, "\nString length = ", len(s4), "charachters")

# 5. Сделайте первые буквы слов строки большими (upper case).
s5 = "one two three four five"
print("5.", s5.title())

# 6. Определите заканчивается ли ваша строка подстрокой “ing”.
s6 = "Doing nothing"
print("6. Is there a '-ing' suffix?", s6.endswith("ing"))

# 7. Определите индекс первого вхождения символа “a” в вашей строке.
s7 = "hgghfdgf hkjgfjhgfbkljsah lakjhshgajkhkljkhajkn"
print("7.", s7.index("a"))

# 8. Разбейте строку на список подстрок по символу пробела.
s8 = "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
print("8.", s8.split())

# 9. Пусть у вас строка имеет пробельные символы. Найдите метод, который удаляет
# пробельные символы вначале и в конце, но не посередине.
s9 = " HHHHHHH HHHHHH HHHHHHH "
print("9.", s9.strip())

# Task_2

# 1. Вычислите длину гипотенузы в прямоугольном треугольнике
# со сторонами 367 и 127.
import math

print("1.", math.hypot(367, 127))

# 2. Дано двузначное число. Найдите число десятков в нем.
n = 87
print("2.", n // 10)

# 3. Дано трёхзначное число. Найдите сумму его цифр.
n = 502
n1 = n // 100
n2 = n % 100 // 10
n3 = n % 10
print("3.", n1 + n2 + n3)

# 4. Дано целое число n. Выведите следующее за ним чётное число.
n = int(input("Enter your number "))
print("4. Next even number is ", (n + 2) - n % 2)
