ug = input("ug oruul: ")
useg = input("useg oruul: ")

while len(useg) != 1 or useg.isdigit():
    print("neg useg oruul")
    useg = input("useg oruul: ")

s = 0
for i in ug:
    if i == useg:
        s += 1

print(s)
