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
        return cls.accounts

    @classmethod
    def find_by_number(cls, number):
        '''
        This method takes in a number and returns a contact that matches that number
        '''

        for account in cls.accounts:
            if account.accountusername == number:
                return account
