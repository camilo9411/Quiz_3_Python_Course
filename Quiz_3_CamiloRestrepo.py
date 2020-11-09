# Name: Camilo Andres Restrepo Rodriguez 
# student ID: 1931815
# Date: 2020/11/09

# ------------------- Quiz # 3 ---------------------

#Class Account
class Account:

    #Constructor
    def __init__(self, balance):

        if (balance>=0):
            self.__balance = round(balance,2)
        else: 
            print('The balance is invalid, we replace it by $ 0.')
            self.__balance = 0

    #Balance property
    def  get__balance(self):
        return self.__balance

    balance = property(get__balance)

    #Credit method
    def Credit(self, amount):
        
        try:
            if amount>0:
                self.__balance =  round(self.__balance + amount,2)
                print('You add ${0} to your account.'.format(amount))
                return True
            else:
                print('The amount must be grater than 0.')
                return False
        except:
            print('Invalid amount. Insert a number.')
            return False

    #Debit Method
    def Debit(self, amount):
        try:
            if amount > 0 and amount <= self.__balance:
                self.__balance = round(self.__balance - amount,2)
                return True
            elif amount < 0:
                print('Amount must be positive.')
                return False
            else:
                print('Debit amount exceeded account balance: ${0}.'.format(self.__balance))
                return False



        except:
            print('Invalid amount. Insert a number.')
            return False


class SavingsAccount(Account):

    def __init__(self, balance, interest_rate):
        super().__init__(balance)
        self.__interest_rate = float(interest_rate/100)

    def CalculateInterest(self):
        return self.balance * self.__interest_rate

class CheckingAccount(Account):

    def __init__(self, balance, fee_per_transation):
        super().__init__(balance)
        if fee_per_transation > 0:
            self.__fee_per_transation = round(fee_per_transation,2)
        else:
            self.__fee_per_transation = 1
    
    def Credit(self, amount):
        
        if Account.Credit(self, amount) == True:
            self._Account__balance = self._Account__balance - self.__fee_per_transation
        
    def Debit(self, amount):
        
        if Account.Debit(self, (amount + self.__fee_per_transation)) == False:
            print('Be sure the amount is smaller than your current value' +
                    'plus the transation fee: ${0}'.format(self.__fee_per_transation))


def main():

    # Testing Class Account
    print('\n\t----- Testing Class Account ------')
    print('\nCreating an Account object with a negative balance...')
    a_1 = Account(-10)
    print(a_1.balance)
    print('\nAdding a negative amount to Account object...')
    a_1.Credit(-10)
    print(a_1.balance)
    print('\nAdding an amount to Account object...')
    a_1.Credit(150.54)
    print(a_1.balance)
    print('\nWithdrawing a negative amount to Account object...')
    a_1.Debit(-50)
    print(a_1.balance)
    print('\nWithdrawing an amount grater than the balance to Account object...')
    a_1.Debit(200)
    print(a_1.balance)
    print('\nWithdrawing an amount to Account object...')
    a_1.Debit(25.247)
    print(a_1.balance)
    # Deleting object
    del a_1

    #Testing class SavingsAccount
    print('\n\t----- Testing Class SavingsAccount ------')
    print('\nCreating an SavingsAccount object...')
    as_1 = SavingsAccount(300,20)
    print(as_1.balance)
    print('\nAdding interest into SavingsAccount object - Option 1...')
    interest = as_1.CalculateInterest()
    as_1.Credit(interest)
    print(as_1.balance)
    print('\nAdding interest into SavingsAccount object - Option 2...')
    as_1.Credit(as_1.CalculateInterest())
    print(as_1.balance)
    # Deleting object
    del as_1

    #Testing class CheckingAccount
    print('\n\t----- Testing Class CheckingAccount ------')
    print('\nCreating an CheckingAccount object...')
    ac_1 = CheckingAccount(10,3)
    print(ac_1.balance)
    print('\nAdding a negative amount to CheckingAccount object...')
    ac_1.Credit(-10)
    print(ac_1.balance)
    print('\nAdding an amount to CheckingAccount object...')
    ac_1.Credit(150)
    print(ac_1.balance)
    print('\nWithdrawing a negative amount to CheckingAccount object...')
    ac_1.Debit(-50)
    print(ac_1.balance)
    print('\nWithdrawing an amount grater than the balance to CheckingAccount object...')
    ac_1.Debit(200)
    print(ac_1.balance)
    print('\nWithdrawing an amount to CheckingAccount object...')
    ac_1.Debit(20)
    print(ac_1.balance)
    # Deleting object
    del ac_1


# Calling main
main()


