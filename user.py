class User:
    """
    Class that generates new instances of users
    """

    pass
#init method to create new instances of a class
    user_list = []
    def __init__(self,first_name,last_name,username,password):

    
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password


    user_list = [] # Empty contact list
 # Init method up here
    def save_user(self):

        '''
        save_user method saves user objects into user_list
        '''

        User.user_list.append(self)