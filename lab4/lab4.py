from bank_accounting import BankAccount

def main():
    account = BankAccount()
    
    while not account.is_blocked():
        user_pin = input("Та пин кодоо оруулна уу: ")
        pin_check = account.check_pin(user_pin)
        
        if pin_check == True:
            while True:
                options = account.menu_options()
                print("\n".join(options))
                user_choice = input("Та ямар үйлчилгээ авах вэ? ")

                if user_choice == "1":
                    amount = int(input("Орлого хийх дүнгээ оруулна уу:  "))
                    account.deposit(amount)
                    print(f"Орлого: {amount}")
                
                elif user_choice == "2":
                    amount = int(input("Та зарлага хийх дүнгээ оруулна уу: "))
                    result = account.withdraw(amount)
                    if result == 'Таны дансны үлдэгдэл хүрэлцэхгүй байна!':
                        print("Таны дансны үлдэгдэл хүрэлцэхгүй байна!")
                    else:
                        print(f"Зарлага: {amount}")
                
                elif user_choice == "3":
                    balance = account.get_balance()
                    print(f"Таны дансны үлдэгдэл: {balance}")

                elif user_choice == "4":
                    receiver_acc = input("Хүлээн авагчийн данс:  ")
                    receiver_name = input("Хүлээн авагчийн нэр: ")
                    amount = int(input("Шилжүүлэх дүн: "))
                    result = account.transfer(receiver_acc, receiver_name, amount)
                    if result == 'Таны дансны үлдэгдэл хүрэлцэхгүй байна!':
                        print("Таны дансны үлдэгдэл хүрэлцэхгүй байна! funds.")
                    else:
                        print(f"Гүйлгээ амжилттай {amount} {receiver_name} ({receiver_acc})")

                elif user_choice == "5": 
                    print("Системээс гарлаа")
                    break

                else:
                    print("Үйлдэлийн алдаа")

        elif pin_check == 'blocked':
            print("3 удаа буруу оруулсан тул пин код блоклогдлоо")
            reset_option = input("1-Пин код сэргээх    2-Орхих")
            if reset_option == '1':
                new_pin = input("Та шинэ пин кодоо оруулна уу: ")
                account.set_new_pin(new_pin)
                account.reset_attempts()
                print("Пин код амжилттай солигдлоо")
            else:
                break
        else:
            print("Пин код буруу байна!")

if __name__ == "__main__":
    main()
