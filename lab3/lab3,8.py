s = ['$2500', '$35500', '$17500', '$4000']

def car(s):
    mashin = []
    mongo = 3300
    for price in s:
        dollar = price.replace("$", "")
        dollar = float(dollar)
        togrog = dollar * mongo
        mashin.append(togrog)
    return mashin

une = car(s)
print(une)
