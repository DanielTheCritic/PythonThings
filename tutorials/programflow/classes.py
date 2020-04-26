# Classes always need at least one thing in them. The pass statement takes care of that
class EmptyClass:
    pass

class TestClass:
    """A Test Class to demonstrate basic use of initializers and methods within a class."""
    # Including an initializer. These also require the self keyword.
    # Initializers are not constructors, and are called once the object is created.
    
    def __init__(self):
        print("hello world from initializer.")

    # Methods in classes require the self parameter. (Which is like this in C#)
    def TestMethod(self):
        print("hello world from method.")

class ComplexClass:
    
    # It's a general rule to have variables that are not intended for direct access. However, everything is public.
    def __init__(self, str):
        self._initString = str
        print(str)

    def TestMethodWithParam(self, str):
        self._initString += ", as called from method. -_-"
        print(self._initString)
        print(str)

# Inheritance of classes is done like below:
class BaseClass:

    def BaseMethod(self):
        print("This is a method from the base class!")

class DerivedClass(BaseClass):
    
    def DerivedMethod(self):
        print("This is a method from the derived class!")

    def DerivedCallingBaseMethod(self):
        self.BaseMethod()
        print("This is a method calling a base method from the derived class!")



