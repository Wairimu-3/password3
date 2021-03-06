import unittest
from credential import Credential
class TestUser(unittest.TestCase):
    def setUp(self):
        """
        Set up method to run before each test cases.
        """
        self.new_credential = Credential("margaret", "royals", "123456", "email@gmail.com")  # create Account obj

    def tearDown(self):
        """
        tearDown method that does clean up after each test case has run.
        """
        Credential.credential_array = []

    def test_init(self):
        """
        test_init test case to test if the object is initialized properly
        """
        self.assertEqual(self.new_credential.credential_name, "margaret")
        self.assertEqual(self.new_credential.usr_name, "royals")
        self.assertEqual(self.new_credential.password, "123456")
        self.assertEqual(self.new_credential.email, "email@gmail.com")

    def test_save_cred(self):
        """
        test_save_cred test case to test if the credential object is saved into
        the credentials array
        """
        self.new_credential.save_credential() 
        self.assertEqual(len(Credential.credential_array), 1)

    def test_display_credentials(self):
        """
        method that returns a list of saved credentials
        """
        self.assertEqual(Credential.display_credential(), Credential.credential_array)


if __name__ == '__main__':
    unittest.main()