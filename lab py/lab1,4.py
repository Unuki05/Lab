username = "admin"
password = "mandakh"

while True:
    user = input("username (esvel 'q' darj garna): ")
    if user.lower() == 'q':
        break

    passw = input("password: ")

    if user == username and passw == password:
        print(f"сайн байна уу? {user} тавтай морил")
        break
    else:
        print("хэрэглэгчийн нэр нууц үг тохирохгүй байна")