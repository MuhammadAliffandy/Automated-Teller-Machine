import os
from module import user as userModules
from module import money as moneyModules
from module import machine as machineModules

def textFormatted(text):
    print('=================================================')
    print(text)
    print('=================================================')


# === LAUNCH APP =====
status = False

while status == False:
    print('WELCOME TO HAPPY MONEY\n')
    print('Please , Sign in or Sign Up with Your Account !!')
    print('=================================================')

    signChoices = ['Sign In' , 'Sign Up']
    for index, sign in enumerate(signChoices):
        print(f'{index + 1}. {sign} ')

    print('=================================================')

    choices = input('Answer with a number: ')

    number = int(choices)

    if(number == 1):
        os.system("cls")
        textFormatted("Sign in with your account")
        username = input('\nUsername: ')
        password = input('Password: ')
        print('\n=================================================')
        response = userModules.User(username,password).readByUserAndPass()
        try:
            if(response['status'] == True):
                print(response['msg'])
                input("\nPlease , press the Enter Button to Next ...")
                os.system("cls")
                status = True
        except:
            os.system("cls")
            print('Username or Password is Wrong !!')
            input("\nPlease , repeat again ...")
            os.system("cls")
            status = False


    elif(number == 2):
        os.system("cls")
        textFormatted("Create your account")
        username = input('\nUsername: ')
        password = input('Password: ')
        print('\n=================================================')
        user = userModules.User(username,password).create()
        moneyModules.Money(user['id']).create(0)
        print(f"\nHalo {user['username']} , Registration is Successfully")
        input("Please , press the Enter Button to Next ...")
        os.system("cls")
        status = False
    else:
        print('\nYour number option is incorrect ')


while status == True:

    user = userModules.User().session()
    Money = moneyModules.Money(user['id'])
    Machine = machineModules.Machine()

    textFormatted(f'HELLO {user["username"]},\nPLEASE, CHOICE YOUR OPTION')

    options = [
        'Check Balance',
        'Cash Deposit',
        'Withdraw Money',
        'Exchange Money',
        'Edit Account',
        'Delete Account',
    ]
    for index, option in enumerate(options):
        print(f'{index + 1}. {option} ')

    print('=================================================')
    choiceOptions = input('Answer with a number: ')

    number = int(choiceOptions)
    if(number == 1):
        Machine.checkBalance(Money)
    elif(number == 2):
        Machine.cashDeposit(Money)
    elif(number == 3):
        Machine.withdrawMoney(Money)
    elif(number == 4):
        Machine.exchangeMoney(Money)
    elif(number == 5):
        Machine.editAccount(userModules,user['id'])
    elif(number == 6):
        Machine.deleteAccount(Money,userModules,user['id'])


    input('Press Enter Button to Back ...')
    os.system("cls")