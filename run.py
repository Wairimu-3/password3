from user import User
from credential import Credential


def create_user(account, user_name, password, email):
    new_user = User(account, user_name, password, email)
    return new_user


def save_user(user):
    user.save_user()


def del_user(user):
    user.delete_user()


def find_user(name):
    return User.find_by_user_name(name)


def check_existing_user(name):
    return User.user_exist(name)


def display_user():
    return User.display_user_name()


def create_credential(credential_name, usr_name, password, email):
    new_credential = Credential(credential_name, usr_name, password, email)
    return new_credential


def save_credential(credential):
    credential.save_credential()


def del_credential(credential):
    credential.delete_credential()


def find_credential(name):
    return Credential.find_by_name(name)


def check_existing_credential(name):
    return Credential.credential_exist(name)


def display_credential():
    return Credential.display_credential()


def main():
    print("Welcome to Password3. What is your name?")
    user_name = input()
    print(f"{user_name}, sign up to create an account.")
    print('\n')

    while True:
        print(
            "Use the short code to continue :\n SU -> SIGN UP.\n DA -> Display your account.\n LN ->LOGIN.\n "
            "ex ->exit Password3. ")

        short_code = input().lower()

        if short_code == 'su':
            print("Welcome. Create a User Account")
            print("_" * 100)
            account = input('Account name:')
            print('\n')
            u_name = input('User name:')
            print('\n')
            pwd = input('Password : ')
            print('\n')
            e_address = input('Email address:')
            save_user(create_user(account, user_name, pwd, e_address))
            print('\n')
            print(f"A New {account} Account with the user name  {u_name} has been created.")
            print(f"You can now login to your {account} account using your password.")
            print('\n')

        elif short_code == 'da':
            if display_user():
                print("Below is your account and details.")
                print('\n')
                for user in display_user():
                    print(f"Account name:{user.user_name}  User name: {user.user_name} Password:{user.password}")
                    print('\n')

            else:
                print('\n')
                print("You dont have an account yet,Sign up to create one")
                print('\n')

        elif short_code == 'ln':
            print("Enter your password to login.")
            search_user = input()

            if check_existing_user(search_user):
                search_cred = find_user(search_user)
                print("\033[1;32;1m   \n")
                print(f"You are now logged in to your {account} account")
                print("\033[1;37;1m   \n")

                while True:
                    print('''
                    Use these short codes:
                    CA -> Create new credential.
                    DC -> Display your credential list
                    ex ->Log out your credential account.''')
                    short_code = input().lower()

                    if short_code == "ca":
                        print("Cool!Create new credential")
                        print('_' * 20)
                        credential_name = input('Credential name:')
                        print('\n')
                        usr_name = input(f"{credential_name} user name:")
                        print('\n')
                        print('*' * 20)
                        pwd = input(f"{credential_name} password:")
                        save_credential(create_credential(credential_name, usr_name, pwd, e_address))
                        print('\n')
                        print(f"A New {credential_name} Account with the user name  {usr_name} has been created.")
                        print('\n')

                    elif short_code == 'dc':
                        if display_credential():
                            print("Here is your credential")
                            print('\n')

                            for credential in display_credential():
                                print(
                                    f"Credential name:{credential.credential_name}  User name: {credential.usr_name} Password:{credential.password}")
                                print('\n')

                        else:
                            print('\n')
                            print("You don't seem to have created any credentials yet")
                            print('\n')

                    elif short_code == "ex":
                        print('\n')
                        print(f"You have logged out of your {account} account")
                        print('\n')
                        break

            else:
                print('\n')
                print("WRONG PASSWORD!! TRY AGAIN?")
                print('\n')
                print('\n')

        elif short_code == "ex":
            print(f"{user_name} Great...Feel free to visit the account again")
            break
        else:
            print("Try using the short codes")


if __name__ == '__main__':
    main()