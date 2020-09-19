#Exception
s = input("Enter: ")
i = 0
try:
    s = int(s) / i
    print(s)
except(ValueError, TypeError) as e:
    print(e)
except ZeroDivisionError as e:
    s = 0
finally:
    print("Goodbye!")

print("Goodbye again!")

while True:
    number = input("Enter a number ")
    try:
        number = float(number)
    except ValueError:
        print("You entered not a number!")
    else:
        break

print(number)
print(type(number))