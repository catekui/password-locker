#!/usr/bin/python3
from user import User, Credentials
import string
from random import randint, random


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

    # main function


def main():
    while True:
        print("Welcome to Password Locker write CA or DA to start")
        print("CA -or- DA")
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
            #save_user(create_user(first_name, last_name, username, accountpassword))
            print("Your user account has been successfully created. These are the details: ")
            print("_" * 10)
            print(f"Name: {first_name} {last_name} \nUsername: {username} \nPassword: {userpassword}")
            print("\nUse Login to your cacount with your details")
            print("\n \n")

        elif option == "DA":
            print("Your Username")
            loginUsername = input()
            print("Your Password")
            loginPassword = input()

            if find_user(loginPassword):
                print("\n")
                print("you can create multiple accounts (MA) and also view them (VA) ")
                print("_" * 60)

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
                        characters = string.ascii_letters + string.digits
                        accountpassword = "".join(random.choice(characters) for x in range(randint(6, 16)))
                        print(f"password: {accountpassword}")
                    elif decision == "C":
                        print("Enter your password")
                        accountpassword = input()
                    else:
                        print("Please put in a valid choice")
                    save_account(create_account(accountusername, accountname, accountpassword))
                    print("\n")
                    print(f"Username: {accountusername} \nAccount Name: {accountname} \nPassword: {accountpassword}")
                elif choose == "VA":
                    if find_account(accountusername):
                        print("Here is a list of your created accounts")
                        print("_" * 25)
                        for user in delete_account():
                            print(f"Account: {user.accountname} \nPassword: {user.accountpassword} \n\n")

                    else:
                        print("Invalid credentials")
                else:
                    print("TRY AGAIN")
            else:
                print("Incorrent info please try again")
                print("\n")
        else:
            print("PLEASE CHOOSE A VALID OPTION")
            print("\n")


if __name__ == '_main_':
    main()
