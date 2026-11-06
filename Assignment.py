class bankaccount:
    def __init__(self,balance):
        self.balance = balance

    def deposit(self,amount):
        self.balance = amount + self.balance
        print("Deposited",amount)
        print("Current Balance",self.balance)

    def withdrawal(self,amount):
        if amount<=self.balance:
            print("Amount Withdrawed:",amount)
            self.balance = self.balance - amount
            print("Current Balance:", self.balance)
        else:
            print("Amount greater than Deposit")

obj1 = bankaccount(3000)
obj1.deposit(30000)
obj1.withdrawal(1000000)
          
    
    
    
