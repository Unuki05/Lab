a = input("та тэмдэгт оруулна:")
b = input("та тоолох тэмдэгтээ оруулна уу: ")
def bibi(a):
    s=0
    for char in a:
         if char==b: 
             s+=1 
    return s
print(bibi("Ur dun"+a))