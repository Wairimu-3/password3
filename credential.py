# credential_array = []
class Credential:
    """
    a class that generates new credential for users
    """
    pass
    credential_array = []

    def __init__(self, credential_name, usr_name, password, email):
        self.credential_name = credential_name
        self.usr_name = usr_name
        self.password = password
        self.email = email

    def save_credential(self):
        """
        save_contact method saves credentials objects into 
        credential_array
        """
        Credential.credential_array.append(self)

    @classmethod
    def display_credential(cls):
        """
        method that returns the credential array
        """
        return cls.credential_array