# Doc strings work a bit like XML comments in C#. They provide metadata about an object.

class TestClassWithDocString: 
    """A class demonstrating how doc strings work."""

    def TestMethod(self):
        """A basic method demonstrating how doc strings work."""
        print("hello world")

print(TestClassWithDocString.__doc__)
print(TestClassWithDocString.TestMethod.__doc__)