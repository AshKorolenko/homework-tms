def factorial(number):
    mul = 1
    for i in range(1, number + 1):
        mul *= i
        return mul
factorial(5)