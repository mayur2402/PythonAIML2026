class bankAccount:
    ROI = 10.5
    def __init__(self,Name,amount):
        self.Name = Name
        self.Amount = amount

    def Display(self):
        print(self.Name)
        print(self.Amount)

    def Deposit(self):
        print("Enter amount to be added")
        amount = float(input())
        self.Amount = self.Amount + amount

    def Withdraw(self):
        print("Enter amount to be withdraw")
        withdraw = float(input())

        if self.Amount < withdraw:
            print("Insuffient balance")
        else:
            self.Amount = self.Amount - withdraw
            print("Withdraw is done")

    def CalculateInterest(self):
        interest = (self.Amount * bankAccount.ROI)/100
        print("Interrest is ",interest)

obj1 = bankAccount("Mayur",10000.00)
obj1.Deposit()
obj1.Withdraw()
obj1.Withdraw()
obj1.CalculateInterest()