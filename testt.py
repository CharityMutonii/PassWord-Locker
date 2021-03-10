import unittest
from credentials import Credentials
class testPassword(unittest.TestCase):
    '''
    Test class that defines test cases for the password behaviour
    '''
    def setUp(self):
        '''
        Set up function to run before each test cases
        unittest.testcase helps in creating tests
        '''
        self.new_credentials= Credentials("twitter","22","22")
    def test_init(self):
        '''
        Function that tests if the object is initialized correctly
        '''
        self.assertEqual(self.new_credentials.app_name,"twitter")
        self.assertEqual(self.new_credentials.password,"22")
        self.assertEqual(self.new_credentials.username,"22")

    def test_save_credentials(self):
        '''
        function that tests if the credential object is saved
        '''
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.credential_list),1)

    def tearDown(self):
        '''
        function hat cleans up after each test case has been run
        '''
        Credentials.credential_list = []

    def test_save_multiple(self):
        '''
        function hat tests if we can save multiple credentials to the credentials list
        '''
        self.new_credentials.save_credentials()
        whatsap_credential = Credentials("twitter","22","charity")
        whatsap_credential.save_credentials()
        self.assertEqual(len(Credentials.credential_list),2)

    def test_delete_credential(self):
        '''
        function that tests if we can delete a credential
        '''
        self.new_credentials.save_credentials()
        whatsap_credential = Credentials("twitter","22","charity")
        whatsap_credential.save_credentials()
        self.new_credentials.delete_credential()
        self.assertEqual(len(Credentials.credential_list),1)
    
    def test_display_all_credentials(self):
        '''
        function that tests if we can return all the credential in credential_list
        '''
        self.assertEqual(Credentials.display_credentials(),Credentials.credential_list)



if __name__ == '__main__':
    unittest.main()
