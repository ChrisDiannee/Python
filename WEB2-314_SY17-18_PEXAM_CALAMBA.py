class bank:
    def __init__(self):
        balance =0
        name = ""
        gender = ""
        age = 0
        address = ""
        work = ""
    def name(self, name):
        bank.name = name
    def gender(self, gender):
        bank.gender =gender
    def age(self, age):
        bank.age = age
    def address(self, address):
        bank.address = address
    def work(self, work):
        bank.work = work  
    def initial(self,balance):  
        bank.balance = balance #this will check balance
    def deposit(self,bal):  #deposit
        bank.balance = bank.balance + bal
    def withdraw(self,wid):
        if self.balance<=0:
            print('You have no money left, please deposit more')
        else:
            bank.balance = bank.balance - wid

class bankingsystem(bank):

    def CreateBankAccount():
        bank1 = bank()                      
        a = input("Full Name: ") 
        bank1.name(a)
        b = input("Gender: ")
        bank1.gender(b)
        c = int(input("Age: "))
        bank1.age(c)
        d = input("Address: ")
        bank1.address(d)
        e = input("Work: ")
        bank1.work(e)

        try:
            ini = int(input("Initial Deposit: "))
            
        except ValueError:
            print("No initial Deposit!")
            return None
        if(ini !=0):
            bank1.initial(ini)
        else:
            print("Not accepted!")


    def manage():
        bank1 = bank()
 
        print("[D] Deposit")
        print("[W] Withdraw\n")
        choice2 = str(input("Please select transaction: "))
        if choice2 == "D":
            bal1 = int(input("Please input amount: "))
            bank1.deposit(bal1)

        elif choice2 == "W":
            bal = int(input("Please input amount: "))
            bank1.withdraw(bal)

        else:
            print("wrong input")

    def main():
        bank1 = bank()
        print("Menu:")
        print("[1] Create Account")
        print("[2] Manage Account")
        print("[3] View account balance\n")


    while(1):
        main()
        bank1 = bank()
        choice = int(input("Please select a number from the above menu: "))

        if choice == 1:
            CreateBankAccount()
        elif choice == 2:
            manage()
        elif choice ==3:
            print("Account balance: " ,bank1.balance)
        else:
            print("Wrong input")







        
