class User:
    """
    Class that generates new instances of users
    """

    # init method to create new instances of a class
    user_list = []

    def __init__(self, first_name, last_name, username, password):

        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password

    # Init method up here

    def save_user(self):

        '''
        save_user method saves user objects into user_list
        '''

        User.user_list.append(self)

    # delete
    def delete_user(self):

        '''
        delete_user method saves user objects into user_list
        '''

        User.user_list.remove(self)

    @classmethod
    def display_users(cls):
        '''
        display_users returns infomation from the user list
        
        '''
        return cls.user_list

    @classmethod
    def find_by_number(cls, number):
        '''
        method that takes in a username and return a user that matches that number
        
        '''
        for user in cls.user_list:
            if user.userpassword == number:
                return user

    @classmethod
    def user_exist(cls, number):
        for user in cls.user_list:
            if user.username == number:
                # return True
                return False

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
