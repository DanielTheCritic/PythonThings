names = [ "Daniel", "Naruto", "Sasuke", "Goku", "Vegeta"]
for n in names:
    print("FOR LOOP: " + n)

count = 0
# len() can be used for getting a length of an array.
while count < len(names):
    x = names[count]
    print("WHILE LOOP: " + x)
    count = count + 1

for n in range(5):
    print("RANGE: " + str(n))

for n in names:
    if n == "Sasuke":
        break
    print("FOR LOOP WITH BREAK: " + n)

for n in names:
    if n == "Sasuke":
        continue
    print("FOR LOOP WITH CONTINUE: " + n)
