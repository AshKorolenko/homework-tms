x = int(input("Please, enter your number: "))
def isPrime(x, div = None):
    if div is None:
        div = x - 1
    while div >= 2:
        if x % div == 0:
            print("The number you entered is not a prime number.")
            return False
        else:
            return isPrime(x, div - 1)
    else:
        print("The number you entered is a prime number.")
        return True
isPrime(x)
