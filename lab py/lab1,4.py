username = "admin"
password = "mandakh"

def check():
    user = input("username: ")
    passw= input("password: ")
    

    if user == username and passw == password:
        print (f"сайн байна уу? {user} тавтай морил")
    else:
        print("хэрэглэгчийн нэр нууц үг тохирохгүй байна")


check()
