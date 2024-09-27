def ihto(x, y, z):
    if x >= y and x >= z:
        return x
    elif y >= x and y >= z:
        return y
    else:
        return z

def bagato(x, y, z):
    if x <= y and x <= z:
        return x
    elif y <= x and y <= z:
        return y
    else:
        return z

def dunto(x, y, z):
    return (x + y + z) / 3

a, b, c = 30, 15, 15

ih = ihto(a, b, c)
baga = bagato(a, b, c)
dun = dunto(a, b, c)

print(f"Хамгийн их: {ih}")
print(f"Хамгийн бага: {baga}")
print(f"Дундаж: {dun}")
