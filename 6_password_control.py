import re

def Check_Password(password):
    if len(password) < 8:
        raise Exception('Password must be at least 7 characters.')
    elif not re.search("[a-z]", password):
        raise Exception('Password must contain lowercase letters.')
    elif not re.search("[A-Z]", password):
        raise Exception('Password must contain uppercase letters.')
    elif not re.search("[0-9]", password):
        raise Exception('Password must contain numbers.')
    elif not re.search("[_@$]", password):
        raise Exception('Password must contain alpha numeric characters.')
    elif re.search("\s", password):
        raise Exception('Password must not contain spaces.')
    else:
        print('Valid password.')

def get_password():
    password = input("Please enter the password: ")
    return password

password = get_password()
try:
    Check_Password(password)
except Exception as Ex:
    print(Ex)
else:
    print('Valid password: Else')
finally:
    print('Validation Completed.')