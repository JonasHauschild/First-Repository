print('Welcome to python.hub Bank ATM')
restart = ('Y')
chances = 3
balance = 999.12
while chances >= 0:
    pin = int(input('Please enter your 4 digit pin: '))
    if pin == (1234):
        print('You entered your pin correctly')
        print('Please press 1 for your balance')
        print('Please press 2 to make a withdrawl')
        while restart not in ['n','NO','no','N']:
            option = int(input('What would xou like to choose?:'))
            if option == 1:
                print('Your balance is $: ', balance)
                restart = input('Would you like to go back? ')
                if restart in ['n', 'NO', 'no', 'N']:
                    print('Thanks')
                    break
            elif option == 2:
                option2 = ('y')
                withdrawl = float(input('How much woul you like to withdrawl? 10, 20, 40, 60, 80, 100: '))
                if withdrawl in [10, 20, 40, 60, 80, 100]:
                    balance -= withdrawl
                    print('\n your balance is now: ', balance)
                    restart = input('Would you like to go back? ')
                    if restart in ('n','NO','no','N'):
                        print('Thanks')
                        break
                elif withdrawl != [10, 20, 40, 60, 80, 100]:
                    print('Invalid amount please tray again')
    elif pin != ('1234'):
        print('Incorrect pin')
        chances -= 1
        if chances == 0:
            print('No more tries')
            break




