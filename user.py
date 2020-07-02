class User:
    """
    a class that generates new instances of users
    """
    pass

    users_array = []

    def __init__(self, first_name, last_name, user_name, password):
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.password = password

    def save_user_details(self):
        """
        save_contact method saves contact objects into user_array
        """
        User.users_array.append(self)

    @classmethod
    def display_users(cls):
        """
        method that returns the class array
        """
        return cls.users_array

    @classmethod
    def user_exist(cls, user_name):
        for user in cls.users_array:
            if user.user_name == user_name:
                return True
        return False  

    @classmethod
    def find_by_user_name(cls, user_name):
        for user in cls.users_array:
            if user.user_name == user_name:
                return user_name    
