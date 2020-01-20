import re

from Model.UserModel import UserModel
from Model.TransactionModel import TransactionModel

user_id_g = 0


class User(UserModel):

    def __init__(self):
        super().__init__()
        self.user_role = ""
        self.user_id = ""

    def login(self, email, password):
        global user_id_g
        result = self.user_authentication(email, password)
        if result:
            self.user_role = result["role"]
            user_id_g = result["_id"]
            if result["role"] == 'A':
                after_login_a()
            elif result["role"] == 'U':
                after_login_n()
        else:
            print("Invalid Credential")

    def getData(self):
        name = input("Enter Name: ")
        if not re.search("^[a-zA-Z ]{1,30}$", name) or len(name) == 0:
            print("\nPlease Enter Valid Name\n")
        email = input("Enter Email: ")
        if not re.search("^[a-z\._]+@[a-z]+\.[a-z]{2,3}$", email) or len(email) == 0:
            print("\nPlease Enter Valid Email\n")
        password = input("Enter Password: ")
        if not re.search("^[a-zA-Z0-9\._]{8,16}$", password) or len(password) == 0:
            print("\nPlease Enter Valid Password\n")
        role = input("Enter Role (A or U) : ")
        if not re.search("^[AU]{1}$", role) or len(role) == 0:
            print("\nPlease Enter Valid Role\n")
        return [name, email, password, role]

    def registration(self):
        user_detail = self.getData()
        print(self.user_registration(user_detail[0], user_detail[1], user_detail[2], user_detail[3]))



class Transaction(TransactionModel):
    def __init__(self):
        super().__init__()
        self.user_role = 'U'
        self.user_id = user_id_g

    def debit(self):
        amount = float(input("Enter Amount for Debit: "))
        print(self.debit_transaction(self.user_id, amount))

    def credit(self):
        amount = float(input("Enter Amount for Credit: "))
        print(self.credit_transaction(self.user_id, amount))

    def customer_amount_detail(self, email):
        print("User Account Balance: \n\n", self.user_transactions(email), "\n\n")

    def user_balance(self):
        print("Your balance :\n\n{0}".format(self.total_balance(user_id_g)))


def before_login():
    user = User()
    print("Welcome TO ABC Bank\n\n1). Login\n2). Registration\n3). Exit\n")
    choice = input("Enter Choice (1, 2, 3): ")
    if choice.isdigit():
        choice = int(choice)
        if choice == 1:
            email = input("Enter Email: ")
            password = input("Enter Password: ")
            user.login(email, password)
        elif choice == 2:
            user.registration()
        elif choice == 3:
            return
        else:
            print("Please enter valid choice")
    else:
        print("Please enter valid choice")


def after_login_n():
    while True:
        transaction = Transaction()
        print("Welcome TO ABC Bank\n\n1). Add\n2). Remove\n3). Total Amount\n4). Logout\n")
        choice = input("Enter Choice (1, 2, 3): ")
        if choice.isdigit():
            choice = int(choice)
            if choice == 1:
                transaction.credit()
            elif choice == 2:
                transaction.debit()
            elif choice == 3:
                transaction.user_balance()
            elif choice == 4:
                return
            else:
                print("Please enter valid choice")
        else:
            print("Please enter valid choice")


def after_login_a():
    while True:
        transaction = Transaction()
        print("Welcome TO ABC Bank\n\n1). Search User Transaction\n2). Logout\n")
        choice = input("Enter Choice (1, 2): ")
        if choice.isdigit():
            choice = int(choice)
            if choice == 1:
                cust_id = input("Enter Customer ID: ")
                transaction.customer_amount_detail(cust_id)
            elif choice == 2:
                return
            else:
                print("Please enter valid choice")
        else:
            print("Please enter valid choice")


while True:
    before_login()
