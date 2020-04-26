import math

def isPrime(number):
    if number < 2:
        return False
    for x in range(2, int(math.sqrt(number) + 1)):
        if number % x == 0:
            return False
    return True

array = [x for x in range(101) if isPrime(x)]
print(array)
