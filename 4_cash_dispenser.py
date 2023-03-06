# Cash Dispenser App

# Here are two sample accounts
account_a = {
    'name': 'abc cba',
    'account_number': '123456',
    'balance': 4000,
    'overdraft': 3000,
}
account_b = {
    'name': 'bcd dcb',
    'account_number': '321321',
    'balance': 3000,
    'overdraft': 1500,
}


def withdrawal(account, quantity):
    print(f"Hello {account['name']}")

    if account['balance'] >= quantity:
        account['balance'] -= quantity
        print('You can withdraw your money')
        balance_inquiry(account)

    else:
        sum = account['balance'] + account['overdraft']
        if sum >= quantity:
            use_overdraft = input('Use additional account? (y/n): ')
            if use_overdraft == 'y':
                amount_to_use_overdraft = quantity - account['balance']
                account['balance'] = 0
                account['overdraft'] -= amount_to_use_overdraft
                print('You can withdraw your money')
                balance_inquiry(account)
            else:
                print(f"You have {account['balance']} balances in your account {account['account_number']}.")
        else:
            print('Sorry, insufficient balance.')
            balance_inquiry(account)


def balance_inquiry(account):
    print(f"You have {account['balance']} TL balances in your account {account['account_number']}. Your overdraft limit is {account['overdraft']} Tl.")



def get_quantity():
    quantity = int(input('How much money do you want to withdraw?: '))
    return quantity


print("Please enter the quantity.")

quantity = get_quantity()

withdrawal(account_a, quantity)

# withdrawal(account_b, quantity)



