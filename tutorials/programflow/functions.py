# Basic function
def func1():
    print("hello world!")

func1()

# Function that takes 2 parameters
def func2(val1, val2):
    print("val1: " + str(val1))
    print("val2: " + str(val2))

func2("test", 123)

# Function that returns a parameter
def func3(val):
    return "This is your value: " + val

print(func3("test"))

# Function like params in C#
def func4(*numbers):
    print(numbers)

func4(1,4,6,19)