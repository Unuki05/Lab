def honog(n):
    hon = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    if n.isdigit():
        num = int(n)
        if 1 <= num <= 7:
            return hon[num - 1]
        else:
            return "1 - 7 hurtleh too oruulna uu, zogsooh bol S"
    else:
        return "1 - 7 hurtleh too oruulna uu, zogsooh bol S"
    
while True:
    r = input("1 - 7 hurtleh too oruulna uu, zogsooh bol S : ")
    if r.upper() == 'S':
        print("zogsson")
        break

    print(honog(r))
