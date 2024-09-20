def sum(*a):
    s=0
    for i in a:
        s+=i
    return s
l= list(map(int,input().split()))
print(sum(*l))
