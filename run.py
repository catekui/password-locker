#!/usr/bin/python3
from user import User

from credentials import Credentials


def create_user(first_name, last_name, username, userpassword):
    newuser = User(first_name, last_name, username, userpassword)
    return newuser


def save_user(user):
    user.save_user()


def delete_user(user):
    user.delete_user()

#
# def find_user(number):
#     return User.find_by_number(number)


def display_users():
    return User.display_users()


def user_exist(username):
    return User.user_exist(username)


def create_account(accountusername, accountname, accountpassword):
    newaccount = Credentials(accountusername, accountname, accountpassword)
    return newaccount


def save_account(user):
    user.save_account()


def delete_account(user):
    user.delete_account()


# def find_account(username):
#     return Credentials.find_by_(username)


def display_accounts():
    return Credentials.display_accounts()


def generate_password():
    return Credentials.generate_password()

    # main function


def main():
    # global accountusername, accountpassword
    while True:
        print("Welcome to Password Locker write create account CA or login LG to start")
        print("CA -or- LG")
        option = input()
        if option == "CA":
            print("create account")
            print("_" * 10)
            print("Enter your First Name")
            first_name = input()
            print("Enter your Last Name")
            last_name = input()
            print("Enter your username")
            username = input()
            print('Set your password')
            userpassword = input()
            save_user(create_user(first_name, last_name, username, userpassword))
            print("Your user account has been successfully created. These are the details: ")
            print("_" * 10)
            print(f"Name: {first_name} {last_name} \nUsername: {username} \nPassword: {userpassword}")
            print("\nUse Login to your account with your details")
            print("\n \n")


        elif option == "LG":
            print("Your Username is..")
            loginUsername = input()
            print("Your Password")
            loginPassword = input()
            confirm_user = user_exist(username)

            if confirm_user == username:

                print("\n")
                print("you can create multiple accounts (MA) and also display accounts(DA)")
                print("_" * 60)
                print("MA -or- DA")

                choose = input()
                if choose == "MA":
                    print("Add your credential account")
                    print("_" * 25)
                    accountusername = loginUsername
                    print("Account Name")
                    accountname = input()
                    print("\n")
                    print("Generate automatic password(G) or Create new password (C)")
                    decision = input()
                    if decision == "G":
                        # characters = string.ascii_letters + string.digits
                        # accountpassword = "".join(choice(characters) for x in range(randint(6, 16)))
                        password = generate_password()
                        print(f"password: {password}")

                    elif decision == "C":

                        print("Enter your password")
                        accountpassword = input()

                    else:
                        print("Please put in a valid choice")
                        save_account(create_account(accountusername, accountname, accountpassword))
                        print("\n")
                        print(f"Username: {accountusername} \nAccount Name: {accountname} \nPassword: {accountpassword}")
                elif choose == "DA":

                    if display_accounts():
                        print("Here is the credential accounts")
                        print('\n')

                        for user in display_accounts():
                            print(f"Account: {user.accountname} \nPassword: {user.accountpassword} \n\n")
                            print('\n')

                    else:
                        print("No credentials or accounts saved")
                
                else:
                    print("Please select either multiple accounts or display accounts")
            else:
                print("Incorrect info please try again")
                print("\n")
        else:
            print("Please choose a valid option")
            print("\n")


if __name__ == '__main__':
    main()
