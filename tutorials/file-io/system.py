import sys

# gets the default encoding
defaultEncoding = sys.getdefaultencoding()
print(defaultEncoding)

text = "this is a line of text\nAnother line of text.\n\nA third line."
print(text)
sys.stdout.write(text)
