def rec_fibonacci(n):
    if n <= 1:
       return n
    else:
        return rec_fibonacci(n - 1) + rec_fibonacci(n - 2)


for n in range(20):
        print(rec_fibonacci(n))
