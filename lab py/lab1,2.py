a = float(input("Ehnii too="))
b = float(input("Daraagiin too="))
c = float(input("Suuliin too="))

if a < b and a < c:
    print("hamgiin baga=", a)
elif b < a and b < c:
    print("hamgiin baga=", b)
elif c < a and c < b:
    print("hamgiin baga=", c)
else:
    print("aldaa")