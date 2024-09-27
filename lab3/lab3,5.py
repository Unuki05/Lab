def ug(word):
    s = word.lower()
    return s == s[::-1]

x = input("Ug: ")
r = ug(x)

print("true" if r else "false")
