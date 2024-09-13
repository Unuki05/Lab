a, b, c = 30, 15, 15

if a >= b and a >= c:
    ih = a
elif b >= a and b >= c:
    ih = b
else:
    ih = c


if a <= b and a <= c:
    baga = a
elif b <= a and b <= c:
    baga = b
else:
    baga = c

dun = (a + b + c) / 3

print(f"Хамгийн их: {ih}")
print(f"Хамгийн бага: {baga}")
print(f"Дундаж: {dun}")
