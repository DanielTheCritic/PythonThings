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

# Function like params in C# called extended arguments syntax or "star args". This is passed in as a Tuple
def func4(*numbers):
    print(type(numbers))
    for i in iter(numbers):
        print(i)

func4(1,4,6,19)

# Function like params in C# but with keywords call "keyword args". Key/value pairs are passed into the method
# to form a dictionary
def func5(name, **kwargs):
    print(name)
    print(type(kwargs))
    print(kwargs)

func5("hello", value="world", counter=150, testcount=2)