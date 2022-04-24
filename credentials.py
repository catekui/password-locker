class Credentials:
    '''
    Class that generates new instances of Credentials
    '''
    accounts= []
    def __init__(self,accountusername,accountname,accountpassword):
        '''
        This method helps us define properties of our object
        '''
    
        self.accountusername = accountusername
        self.accountname = accountname
        self.accountpassword = accountpassword
        #saving method
    def save_account(self):
        '''
        save_account method saves user info into accounts
        '''

        Credentials.accounts.append(self)

    def delete_account(self):
        '''
        delete_account method deletes user info from the accounts
        '''

        credentials.accounts.remove(self)
    
        
