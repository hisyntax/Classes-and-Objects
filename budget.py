class Budget():
    balance = 0
    def __init__(self, budget_category):
        self.budget_category = budget_category
    def getCategoryName(self):
        return self.budget_category
    def depositFunds(self):
        print('Deposit Fund into', self.budget_category)
        amount = int(input(''))
        self.balance += amount
        print('your ', self.budget_category, ' balance is: ', self.balance)
    def withdrawFunds(self):
        amount = int(input('Withdraw Fund \n ' ))
        if(amount > self.balance):
            print('Insufficient Funds')
            amount = int(input('Try withdrawing a lesser amount \n ' ))
            if(amount > self.balance):
                print('Try Again')
            else: 
                print('done')
        else:
            self.balance -= amount
            print('done')
    def getBalance(self):
        print('Your ', self.budget_category, 'balance is: ', self.balance)
    def transferFundTo(self, amount):
        if(amount > self.balance):
            return False
        else:
            self.balance -= amount
            return True
    def receiveFunds(self, amount):
        self.balance += amount
        print(self.budget_category, 'balance is now:', self.balance)

def transferFunds(fro, to, transferAmount):
    print('Transferring ', transferAmount, 'from ', fro.getCategoryName(), ' to', to.getCategoryName() )
    if(fro.transferFundTo(transferAmount)):
        to.receiveFunds(transferAmount)
        print('You have successfully transferred ', transferAmount, 'to ', to.getCategoryName())
    else: 
        print('Can\'t transfer funds because of insufficient fund')
food = Budget('food')
clothing = Budget('clothing')
entertainment = Budget('entertainment')
food.depositFunds()
entertainment.depositFunds()
clothing.depositFunds()
transferFunds(food, clothing, 500)