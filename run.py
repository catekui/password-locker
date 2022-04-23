

from user import User

def create_user(first_name, last_name, username, password):
    newuser = User(first_name, last_name, username, password)
    return newuser

def save_user(user):
    user.save.user()

def delete_user(user):
    user.delete_user()

def find_user(number):
    return User.find_by_number(number)

def display_users():
    return User.display_users()

def create_account(accountusername, accountname, accountpassword):
    newaccount = Credentials(accountusername, accountname, accountpassword)
    return newaccount

def save_account(user):
    user.save_account()

def delete_account(user):
    user.delete_account()

def find_account(number):
    return Credentials.find_by_number(number)

def display_accounts():
    return Credentials.display_accounts()

    

