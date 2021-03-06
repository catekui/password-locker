import unittest
from user import User  # Importing the user class


class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.user_list = []

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Cate", "Wangui", "Cate", "@Kate")  # create  object

    def test_init(self):
        '''
        test_init test to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.username, 'Cate')

        self.assertEqual(self.new_user.password, '@Kate')

    # function for saving users
    def test_save_user(self):
        '''
        test_save_user to test if the user object is saved in the user list
        '''
        self.new_user.save_user()  # saving the new user
        self.assertEqual(len(User.user_list), 1)

    # function to delete the user
    # def test_delete_user(self):
    #     '''
    #     test_delete_user to delete the user from the user list
    #     '''
    #     self.new_contact.save_contact()
    #     test_user = User("Test", "user", "1234567890" "test@kate")
    #     test_user.save_user()
    #
    #     self.new_user.delete_user()  # delete the user object
    #     self.assertEqual(len(User.user_list), 1)


if __name__ == '__main__':
    unittest.main()
