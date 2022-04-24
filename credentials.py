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
    
        
