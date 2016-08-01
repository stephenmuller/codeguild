"""ATM Program"""


import account

def create_account():
    """makes some test accounts"""
    stephen_checking = Account()
    stephen.account_type = 'checking'
    stephen.user_id = 'stephen_checking'
    stephen.deposit = 5
    stephen_savings = Account()
    stephen.account_type = 'saving'
    stephen.user_id = 'stephen_savings'
    stephen.deposit = 500000000
    return stephen_checking, stephen_savings


def main_menu():
    """Main menu module"""
    return input(
        'welcome to bank, \n' +
        'press 1 to get balance \n' +
        'press 2 to deposit money \n' +
        'press 3 to withdraw cash \n' +
    )


def specify_account():
    """asks the user what account they would like to access"""
    return(
        'Which account would you like to access? \n' +
        'Press 1 for checking \n' +
        'Press 2 for savings'
    )


def main_menu_tree(menu_option_number, checking, savings):
    """picks the function the user called for"""
    menu_option_number = main_menu()
    account_to_use = specify_account()

    if menu_option_number == '1':
        if account_to_use == '1':
            print(checking.getfunds)
        else:
            print(savings.getfunds)

    elif menu_option_number == '2':


    elif menu_option_number == '3':

    else:
        ##ask if they want to do something else




def main():
    """main"""
    stephen_checking, stephen_savings = create_account()
    main_menu_tree(stephen_checking, stephen_savings)



