import random
import string

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
    def find_by_username(cls, username):
        '''
        method that takes in a username and return a user that matches that username
        
        '''
        for user in cls.user_list:
            if user.username== username:
                return user

    @classmethod
    def user_exist(cls, username):
        active_user = ""
        for user in User.user_list:
            if user.username == username:
                active_user = user.username
        return active_user
                # return True
                # return False

