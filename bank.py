import random
from datetime import datetime

database = {}


def home():
    print("Welcome to AZBank")
    while True:
        hasAccount = int(input("Do you have an account with us? 1 (yes) 2 (No)\n"))
        if hasAccount == 1:
            login()
        elif hasAccount == 2:
            register()
        else:
            print("You have selected an invalid option, please try again")


def login():
    print("Please Login with your details \n")
    loginSuccessful = False
    while not loginSuccessful:
        userAcctNumber = input("Please enter your Account Number \n")
        is_valid_AcctNumber = acctNumberValidation(userAcctNumber)

        if is_valid_AcctNumber:

            userPassword = input("Please enter your Password \n")

            for acctNumber, userDetails in database.items():
                if acctNumber == int(userAcctNumber):
                    if userDetails[3] == userPassword:
                        loginSuccessful = True
                        operations(acctNumber)

            if not loginSuccessful:
                print("Invalid Account Number or Password")
        else:
            home()


def acctNumberValidation(acctNumber):
    # check if account Number is not empty
    # check if account Number is 10 digit
    # check if account Number is an integer

    if acctNumber:

        if len(str(acctNumber)) == 10:

            try:
                int(acctNumber)
                return True
            except ValueError:
                print("Invalid Account Number")
                return False
            except TypeError:
                print("Invalid Account Number")
                return False

        else:
            print("Account Number must be 10 digit")
            return False

    else:
        print("Please enter Account Number \n")
        return False


def register():
    print("Please sign up for an account")
    email = input("Email Address \n")
    firstName = input("First Name \n")
    lastName = input("Last Name \n")
    password = input("Password \n")
    amountDeposited = 0

    acctNumber = generateAccNumber()

    database[acctNumber] = [firstName, lastName, email, password, amountDeposited]
    print("Your Account Number has been created \n")
    print(acctNumber)
    login()


def generateAccNumber():
    print("Account number")
    return random.randrange(2222222222, 8888888888)


def operations(acctNumber):
    firstName, lastName = database[acctNumber][:2]
    print("Welcome %s %s " % (firstName, lastName))
    print("What would you like to do? \n")
    while True:
        options = int(input("1. Deposit 2. Withdrawal 3. Check Account Balance 4. Log Out 5.Exit \n"))
        if options == 1:
            deposit(acctNumber)
        elif options == 2:
            withdrawal(acctNumber)
        elif options == 3:
            accountBalance(acctNumber)
        elif options == 4:
            login()
        elif options == 5:
            break
        else:
            print("Invalid option selected")


def deposit(acctNumber):
    amountDeposit = int(input("Please make a deposit \n"))
    database[acctNumber][4] += amountDeposit
    print("Thanks for making a deposit \n")
    print("Your account balance is  %s" % database[acctNumber][4])


def withdrawal(acctNumber):
    amountWithdraw = int(input("How much would you like to withdrawals \n"))
    if amountWithdraw > database[acctNumber][4]:
        print("Insufficent Funds... Please make a deposit")
    else:
        database[acctNumber][4] -= amountWithdraw
        print("Please take your cash")
        print("Your account balance is %s" %database[acctNumber][4] )


def accountBalance(acctNumber):
    print('Your account balance is %s' % database[acctNumber][4])


if __name__ == "__main__":
    home()

