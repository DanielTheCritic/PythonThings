print("Testing Operators.")

x = 5
y = 3

# Using str() is required when doing concatenation with strings.
# Addition
print ("Add: " + str(x + y))
# Subtraction
print ("Subtract: " + str(x - y))
# Multiplication
print ("Multiply: " + str(x * y))
# Division
print ("Divide: " + str(x / y))
# Division and round off
print ("Divide: " + str(x // y))
# Exponent
print ("Exponent: " + str(x ** y))
# Modulus
print ("Modulus: " + str(x % y))

# Equals comparison
if x == 5:
    print("X == 5")

# Not Equals comparison
if x != 2:
    print("X != 2")

# Greater than comparison
if x > 1:
    print("X > 1")

# Less than comparison
if x < 10:
    print("X < 10")

# Less than or equal to comparison
if x <= 5:
    print("X <= 5")

# Greater than or equal to comparison
if x >= 5:
    print("X >= 5")

# And clause
if x == 5 and y == 3:
    print("x == 5 and y == 3")

# Or clause
if x == 5 or y == 3:
    print("x == 5 or y == 3")

# Not clause
if not x == 3:
    print("not x == 3")

# Elif clause
if x == 6:
    print("x == 6")
elif x == 5:
    print ("Elif x == 5")

# Else clause
if x == 6:
    print("x == 6")
else:
    print ("else")
