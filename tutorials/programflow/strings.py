stringval = "Hello World"

print("Original: " + stringval)
print("Upper case: " + stringval.upper())
print("Lower case: " + stringval.lower())
print("String length: " + str(len(stringval)))
print("First 3 letters: " + stringval[0:3])
print("First 3 letters (alternate): " + stringval[:3])
print("Last 3 letters: " + stringval[len(stringval) - 3 : len(stringval)])
print("Last letter: " + stringval[-1])
print("Is First Letter Upper Case: " + str(stringval[:1].isupper()))
print("Is First Letter Lower Case: " + str(stringval[:1].islower()))
print("Is First Letter Alphanumeric: " + str(stringval[:1].isalpha()))
print("Is First Letter A Number: " + str(stringval[:1].isdigit()))

val = "test"
val2 = 1234
fString = f'This is an f-string with val: {val} and val2: {val2}'
print(fString)

formatString = "This is a format string with val: {0} and val2: {1}".format(val, val2)

data = (5, "test", "hello")
print("I am doing clever formatting with tuples and values: %i and %s and %s" % data)

joinString = " ".join(["hello", "my", "world"])
print(f"Join statement: {joinString}")

partitionString = "unforgetable".partition("forget")
print(f"Tuple of partitioned strings: {partitionString}")

origin, _, destination = "unforgetable".partition("forget")
print(f"Partitioned strings without partition: {origin, destination}")

longString = "This is a long string " \
            "that is concatenated over " \
            "multiple lines"
print(longString)