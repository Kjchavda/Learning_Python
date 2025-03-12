a = input("Enter a number: ")
b = input("Enter another number: ")

try:
    print(int(a)/int(b))
except ZeroDivisionError:
    print("Cant divide by zero")
except ValueError:
    print("Enter a valid value")
finally:
    print("The finally block always executes!")
