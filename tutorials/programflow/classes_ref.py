from classes import EmptyClass
from classes import TestClass
from classes import ComplexClass as complex
from classes import DerivedClass

# Creating an instance of the class
c = EmptyClass()
print(type(c))

# Calling instance methods
t = TestClass()
# Long way (not really used)
TestClass.TestMethod(t)
# Shorthand
t.TestMethod()

# Calling classes with initializers
ti = complex("my initializer string")
ti.TestMethodWithParam("my method string")

# Calling classes with inheritance.
derived = DerivedClass()
derived.BaseMethod()
derived.DerivedMethod()
derived.DerivedCallingBaseMethod();
