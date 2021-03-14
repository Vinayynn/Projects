class Bank:
    
    def createAccountDetails(self):
        self.accountNumber = int(input("Enter the account number :"))
        self.accountName = input("Enter the account holder's name :")
        self.branch = input("Enter the branch :")
        self.balance = 1000000
        self.withdrawAmount = 0
        self.depositAmount = 0
    
    def displayAccountDetailsFunction(self):  
        print("-"*50)
        print("The account holder is",self.accountName)
        print("The account number is",self.accountNumber)
        print("The branch is",self.branch)
        print("The balance in your account is",self.balance)
        print("-"*50)

    def withdrawFunction(self):
        self.withdrawAmount = int(input("Enter the money to be with drawn :"))
        if self.withdrawAmount >= self.balance:
            print("-"*50)
            print("Account ge kaas haako koth nan magne. . . . .")
            print("-"*50)
        else:
            self.balance = self.balance - self.withdrawAmount
            print("-"*50)
            print("You have withdrawn Rs{} from your account and the balance is Rs{}".format(self.withdrawAmount, self.balance))
            print("Thank you for transacting with us, Please visit again!")
            print("-"*50)

    def depositFunction(self):
        self.depositAmount = int(input("Enter the money to be deposited :"))
        self.balance = self.balance + self.depositAmount
        print("-"*50)
        print("You have deposited Rs{} to your account and the balance is Rs{}".format(self.depositAmount, self.balance))
        print("Thank you for transacting with us, Please visit again!")
        print("-"*50)


b1 = Bank()
b1.createAccountDetails()
b1.displayAccountDetailsFunction()

wORd = input("Do you want to withdraw or deposit.(Answer with 'w' or 'd' or 'n') :")

if wORd == 'w':
    b1.withdrawFunction()
    print("-"*50)

elif wORd == 'd':
    b1.depositFunction()
    print("-"*50)

else:
    print("-"*50)
    print("Thank you for transacting with us, Please visit again!")
    print("-"*50)