class Account():


    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    def deposit(self,amount):
        self.balance = self.balance + amount
        print(f"Amount deposited : {amount}")

    def withdraw(self,wd_amount):
        if self.balance >= wd_amount:
            self.balance = self.balance - wd_amount
            print(f"Amount withdrawn : {wd_amount}")
        else:
            print("Sorry! Have no suffiecient balance.")

    def __str__(self):
        return f"Owner : {self.owner} \nBalance : {self.balance} "
            

myobj = Account('Rony',800)
print(myobj.owner)
print(myobj.balance)
print(myobj)
print(myobj.deposit(500))
print(myobj)
print(myobj.withdraw(800))
print(myobj)



