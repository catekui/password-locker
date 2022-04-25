import random
import string


class Credentials:
    '''
    Class that generates new instances of Credentials
    '''
    accounts = []

    def __init__(self, accountusername, accountname, accountpassword):
        '''
        This method helps us define properties of our object
        '''

        self.accountusername = accountusername
        self.accountname = accountname
        self.accountpassword = accountpassword
        # saving method

    def save_account(self):
        '''
        save_account method saves user info into accounts
        '''

        Credentials.accounts.append(self)

    def delete_account(self):
        '''
        delete_account method deletes user info from the accounts
        '''

        Credentials.accounts.remove(self)

    @classmethod
    def display_accounts(cls):
        '''
        method that returns the list of the accounts
        '''
        # for account in cls.accounts:
        #     return cls.accounts
        return cls.accounts

    @classmethod
    def find_by_username(cls, username):
        '''
        method that takes in a username and return a user that matches that username
        
        '''
        for user in cls.accounts:
            if user.username == username:
                return user

    def generate_password(size=8, char=string.ascii_uppercase + string.ascii_lowercase + string.digits):
        return "".join(random.choice(char)
                       for _ in range(size))
