from lab4 import *
class Nem:
    def check_pin(self):
            while self.a > 0:
                self.Userpin = input("Та пин кодоо оруулна уу: ")
                if self.Userpin == self.pin:
                    self.menu()
                else:
                    print("Пин код буруу байна!")
                    self.a -= 1
                    if self.a == 0:
                        print("3 удаа буруу оруулсан тул пин код блоклогдлоо")
                        print("1-Пин код сэргээх    2-Орхих")
                        self.pin_restore()
                        self.menu()
                        break
    def menu(self):
            while self.loop:
                        print("1-Орлого хийх   2-Зарлага хийх  3-Үлдэгдэл шалгах  4-Шилжүүлэг хийх  5-Гарах")
                        inp = input("Та ямар үйлчилгээ авах вэ? ")
                        if inp =="1":
                            self.deposit()
                        elif inp =="2":
                            self.withdraw()
                        elif inp == '3':
                            self.vldegdel()
                        elif inp =='4':
                            self.transit()
                        elif inp == "5":
                            print("Системээс гарлаа.")
                            self.conX()
                        else:
                            print("Үйлдэлийн алдаа!")
    def trans_t(self):
            self.dns=input('Хүлээн авагчийн данс: ')
            self.ner=input('Хүлээн авагчийн нэр: ')
            self.dvn=int(input('Шилжүүлэх дүн: '))
            self.conX()
            self.trans_t()
            print('-------------------')
            print(f'Хүлээн авагчийн данс:{self.dns}')
            print(f'Хүлээн авагчийн нэр:{self.ner}')
            print(f'Шилжүүлэх дүн:{self.dvn}')
            print('-------------------')
            print("1-Үргэлжлүүлэх   2-Засварлах")
            if(self.dvn>self.vld):
                print('Таны дансны үлдэгдэл хүрэлцэхгүй байна!')
                self.conY()
                self.again2()
            elif self.contin == '2':
                self.trans_t()
                self.again()
            else:
                print("Үйлдэлийн алдаа")
        
    def conX(self):
        self.loop = False
        self.a = 0
    def conY(self):
        self.loop = True
        self.a = 3
    def pin_restore(self):
            self.res=input("")
            if(self.res == '1'):
                print('Та шинэ пин кодоо оруулна уу: ')
                self.NewPin=input("")
                self.pin = self.NewPin
                print('Пин код амжилттай солигдлоо')
                self.again()

    def again(self):
        print("Гүйлгээ амжилттай")
        print('1-Дахин гүйлгээ хийх     2-Гарах')
        self.ag = input('')
        if self.ag == '1':
            self.conY()
            self.menu()
        elif self.ag == '2':
            print('Системээс гарлаа')
        else:
            print("Үйлдэлийн алдаа")
    def again2(self):
        print('1-Дахин гүйлгээ хийх     2-Гарах')
        self.ag = input('')
        if self.ag == '1':
            self.conY()
            self.menu()
        elif self.ag == '2':
            print('Системээс гарлаа')
        else:
            print("Үйлдэлийн алдаа")