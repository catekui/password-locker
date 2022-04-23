import unittest 
from user import User # Importing the contact class

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the contact class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User(first_name, last_name, username, password)("Cate","Wangui","Sweetcate","@Kate") # create contact object


def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_contact.first_name,"Cate")
        self.assertEqual(self.new_contact.last_name,"Wangui")
        self.assertEqual(self.new_contact.username,"Sweetcate")
        self.assertEqual(self.new_contact.password,"@Kate")


if __name__ == '__main__':
    unittest.main()

    #test for saving users
    def test_save_user(self):
        '''
        test_save_user test case to test if the contact object is saved into
         the user list
        '''
        self.new_user.save_user() # saving the new user
        self.assertEqual(len(User.user_list),1)
# test for saving multiple users
    def test_save_multiple_user(self):
            '''
            test_save_multiple_user to check if we can save multiple user
            objects to our user_list
            '''
            self.new_user.save_user()
            test_user = user("Test","user","0712345678","test@user.com") # new user
            test_user.save_user()
            self.assertEqual(len(user.user_list),2)
#tearDown method
    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            User.User_list = []

# other test cases here
    def test_save_multiple_user(self):
            '''
            test_save_multiple_user to check if we can save multiple user
            objects to our user_list
            '''
            self.new_user.save_user()
            test_user = User("Test","user","username","password") # new user
            test_user.save_user()()
            self.assertEqual(len(User.user_list),2)
#delete method test
    def test_delete_user(self):
            '''
            test_delete_user to test if we can remove a user from our user list
            '''
            self.new_contact.save_contact()
            test_User = User("Test","user","username","password") # new user
            test_User.save_user()

            self.new_user.delete_user()# Deleting a user object
            self.assertEqual(len(User.user_list),1)

