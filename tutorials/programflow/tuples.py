# A basic tuple is declared with regular brackets
myTuple = ("value1", 1234)

# A nested tuple can be created
myNestedTuple = ("value1", (1234, "Another test value", True))

# Tuples can be unpacked with what's known as Tuple Unpacking below
x, y = myTuple
print(x)
print(y)

nx, ny = myNestedTuple
ny1, ny2, ny3 = ny

print(nx)
print(ny1)
print(ny2)
print(ny3)