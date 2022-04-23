import unittest 
from user import User # Importing the user class

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User()("Cate","Wangui","Sweetcate","@Kate") # create  object

def test_init(self):
        '''
        test_init test to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.username,'Cate')

        self.assertEqual(self.new_user.password, '@Kate')
#function for saving users

