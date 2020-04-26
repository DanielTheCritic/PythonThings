# Modes: r = open for reading, w = open for writing, a = open for appending
# Selector: b = binary mode, t = text mode
# E.G wb = write binary, at = append text

f = open("myfile.txt", mode="wt")
f.write("This is the content of my new text file.\nThis is another line.\n")
f.close()

f = open("myfile.txt", mode="rt", encoding="utf-8")

text = f.read() # Reads whole file
print(text)
f.close()

f = open("myfile.txt", mode="rt", encoding="utf-8")
textCharacters = f.read(12) # Reads the first 12 characters
print(textCharacters)

textCharacters = f.read(10) # Reads the next 10 characters
print(textCharacters)

f.seek(0) # Moves pointer back to the beginning of the file
textCharacters = f.read(15) # Reads the first 15 characters
print(textCharacters)

f.seek(0)
textLine = f.readline() # Reads a single line
print(textLine)
textLine = f.readline() # Reads the next line
print(textLine)

f.seek(0)
textLines = f.readlines() # Reads all the lines
print(textLines)

f.close()

# Appending allows for writing lines to the end of a file
f = open("myfile.txt", mode="at", encoding="utf-8")
f.writelines(["This is another line\n", "This is yet another line\n"])
f.close()

# with-blocks are contextual blocks like using blocks that implement a try/except/finally and try/finally under the hood
with open("myfile.txt", mode="rt", encoding="utf-8") as f:
    text = f.read()
    print(text)




