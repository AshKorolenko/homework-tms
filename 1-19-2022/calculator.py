def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


import math


print("Please, select an operation: \n"
    "1. Add\n"
    "2. Subtract\n"
    "3. Multiply\n"
    "4. Divide\n"
    "5. Sine\n"
    "6. Cosine\n"
    "7. Tangent\n")


while True:

    choice = int(input("Select operations 1, 2, 3, 4, 5, 6, 7: "))
    x = input("Enter the first number: ")
    if x.isdigit():
        x = float(x)
    else:
        print("Invalid input. Enter a number.")
        continue
    if choice == 5:
        print(math.sin(x))
    elif choice == 6:
        print(math.cos(x))
    elif choice == 7:
        print(math.tan(x))
        next_calculation = input("Would you like to proceed? (yes/no): ")
        if next_calculation == "no":
            break
    else:
        y = input("Enter the second number: ")
        if y.isdigit():
            y = float(y)
        else:
            print("Invalid input. Enter a number.")
            continue

        if choice == 1:
            print(x, "+", y, "=", add(x, y))

        elif choice == 2:
            print(x, "-", y, "=", subtract(x, y))

        elif choice == 3:
            print(x, "*", y, "=", multiply(x, y))

        elif choice == 4:
            if y == 0:
                print("Error: division by zero.")
            else:
                print(x, "/", y, "=", divide(x, y))

        else:
            print("Invalid input.")

        next_calculation = input("Would you like to proceed? (yes/no): ")
        if next_calculation == "no":
            break
