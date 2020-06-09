numbers = [1, 5, 9, 11]

doubler = lambda n: n * 2
adder = lambda x, y: x + y

for number in numbers:
    print(doubler(number))
    print(adder(number, 1))