class BankAccount:
    def __init__(self): 
        self.__attempts = 3    
        self.__pin = "2005"     
        self.__balance = 0     

    def check_pin(self, user_pin):
        self.__balance = 100
        if user_pin == self.__pin:
            return True
        else:
            self.__attempts -= 1
            if self.__attempts == 0:
                return 'blocked'
            return False
    
    def is_blocked(self):
        return self.__attempts == 0

    def reset_attempts(self):
        self.__attempts = 3

    def set_new_pin(self, new_pin):
        self.__pin = new_pin

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            return 'insufficient_funds'
        else:
            self.__balance -= amount
            return 'success'

    def get_balance(self):
        return self.__balance

    def transfer(self, receiver_acc, receiver_name, amount):
        if amount > self.__balance:
            return 'insufficient_funds'
        else:
            self.__balance -= amount
            return receiver_acc, receiver_name, amount

    def menu_options(self):
        return ["1-Орлого хийх", "2-Зарлага хийх", "3-Үлдэгдэл шалгах", "4-Шилжүүлэг хийх", "5-Гарах"]
