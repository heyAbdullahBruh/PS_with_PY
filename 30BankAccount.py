# problem-30 ---> Create bank account classess method-->

class BankAccount  :
    userName =''
    ammount=0
    
    def __init__(self,userName,ammount):
       self.userName=userName
       self.ammount=ammount
       
    def details(self):
             return{"name":self.userName,"balance": self.ammount}

    def deposit (self,depAmmount):
        self.ammount = self.ammount + depAmmount
        return f'You added {depAmmount}. Your current balance is = {self.ammount}'
    
    def withdraw (self,wdAmmount):
        self.ammount = self.ammount -wdAmmount
        return f'You withdraw {wdAmmount}. Your current balance is = {self.ammount}'
    
    def showBalance(self):
        return f'Hey Hey {self.userName}. Your current balance is = {self.ammount}'

tareksBankAcc = BankAccount('TarekulRifat',40000)

print(tareksBankAcc.showBalance()) #Hey Hey TarekulRifat. Your current balance is = 40000
print(tareksBankAcc.withdraw(3000))#You withdraw 3000. Your current balance is = 37000   
print(tareksBankAcc.showBalance())#Hey Hey TarekulRifat. Your current balance is = 37000
print(tareksBankAcc.deposit(5000))#You added 5000. Your current balance is = 42000      
print(tareksBankAcc.details())#{'name': 'TarekulRifat', 'balance': 42000}
