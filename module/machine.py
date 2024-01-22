import os

def textFormatted(text):
    print('=================================================')
    print(text)
    print('=================================================')

class Machine:

# check balance
    @staticmethod
    def checkBalance(Money):
        os.system("cls")
        response = Money.read()
        rupiah_string = "Your Balance Now: Rp {:,.0f}".format(float(response['data']))
        textFormatted(rupiah_string)

# cash deposit
    @staticmethod
    def cashDeposit(Money):
        os.system("cls")
        response = Money.read()
        cash = int(input('Add your cash deposit value: '))
        if(response['data'] > 0):
            Money.update(cash,'DEPOSIT')
            response = Money.read()
        else:
            Money.create(cash)
            response = Money.read()
        os.system("cls")
        rupiah_string = "Your Balance Now: Rp {:,.0f}".format(float(response['data']))
        textFormatted(rupiah_string)

# withdraw money
    @staticmethod
    def withdrawMoney(Money):
        os.system("cls")
        response = Money.read()

        textFormatted('CHOICE YOUR NUMBER OPTION')
        optionNumber = [20000,50000,100000]

        for index, option in enumerate(optionNumber):
            print(f'{index + 1}. {option} ')

        option = int(input('Choice the number: '))
        os.system("cls")

        cash = int(input('Add your withdraw value: '))
        
        if(cash % optionNumber[option -1] > 0):
            textFormatted('YOUR NUMBER INPUT IS INCORRECT FOR THE OPTION')
        else:
            if(response['data'] <= 25000):
                textFormatted('YOUR BALANCE IS NOT ENOUGH')
            else:
                Money.update(cash,'PULL')
                response = Money.read()
                
            os.system("cls")
            rupiah_string = "Your Balance Now: Rp {:,.0f}".format(float(response['data']))
            textFormatted(rupiah_string)

#Exchange Money
            
    @staticmethod
    def exchangeMoney(Money):
        os.system("cls")

        textFormatted('CHOICE YOUR NUMBER OPTION')
        optionType = ['MALAYSIA','JAPAN','KOREA','USA']

        for index, option in enumerate(optionType):
            print(f'{index + 1}. {option} ')

        option = int(input('Choice the number: '))
        os.system("cls")
        
        cash = int(input(f'Add your Money from {optionType[option - 1]} :'))

        moneyType = ''
        if(option == 1):
            moneyType = 'MLY'
        elif(option == 2):
            moneyType = 'JPN'
        elif(option == 3):
            moneyType = 'KOR'
        elif(option == 4):
            moneyType = 'USA'

        value = Money.exchange(cash,moneyType)

        os.system("cls")
        rupiah_string = "The Money exchange to : Rp {:,.0f}".format(float(value))
        textFormatted(rupiah_string)

#Edit account 
    @staticmethod
    def editAccount(userModules,userId):
        os.system('cls')
        textFormatted('Edit Your Account')

        username = input('\nUsername :')
        password = input('Password: ')

        print('\n=================================================')

        editUser = userModules.User(username,password).edit(userId)

        if(editUser):
            print('\nEdit Account is Successfully')
        else:
            print('\nYour Account is Not Found\n')

#Delete Account
    @staticmethod
    def deleteAccount(Money,userModules,userId):
        os.system('cls')
        textFormatted('Delete Account')
        answer = input('Are you sure to delete your account (y/n): ')
        
        if(answer == 'y' or answer == 'Y'):
            userModules.User().delete(userId)
            Money.delete()
            print('Okay your account has been deleted now\n')
            os.system('cls')
        elif(answer == 'n' or answer == 'N'):
            print('Okay, next your activity')
        else:
            print('Sorry, your input is wrong')