import json
import re
from pathlib import Path
import hashlib

class Validation:
    email_compiler = re.compile(
        "^([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+$")
    password_compiler = re.compile(
        "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$")
    global_phone_compiler = re.compile(
        "^+(?<country>\d{1,3})-(?<prefix>\d{2,3})-(?<number>\d{3}-\d{2}-\d{2})")
    accepted_countries = {'994': 'Azerbaijan', '90': 'Turkey'}

    def __init__(self):
        pass

    def validate_name(self, value):
        return value.isalpha()

    def validate_surname(self, value):
        return value.isalpha()

    def validate_key(self, value):
        if len(value) <= 15:
            return value.isalpha()

    def validate_mail(self, value):
        return bool(self.email_compiler.match(value))

    def validate_password(self, value):
        return bool(self.password_compiler.match(value))

    def validate_phone(self, value):
        match = self.global_phone_compiler.match(value)
        if match:
            groupdict = match.groupdict()
            country, prefix, number = groupdict['country'], groupdict['prefix'], groupdict['number']
            if country not in self.accepted_countries:
                return False
            else:
                # return self.accepted_countries.get(country)
                return True
        else:
            return False


class Encryption:
    def __init__(self):
        pass

    def hashing(self, value):
        return str(hashlib.sha512(value.encode()).hexdigest())


class JSONStorage:
    init_data = {'users': []}

    def __init__(self, filename='passwords.json'):
        self.path = Path(filename)
        self._initilize_file()

    def _get_users(self):
        with open(self.path, mode='r', encoding='UTF-8') as file:
            content = json.load(file)

        return content.get('users')

    def _save_new_users(self, new_users):
        new_content = {'users': new_users}
        with open(self.path, mode='w', encoding='UTF-8') as file:
            json.load(new_content, file)

    def _initilize_file(self):
        if not self.path.exists():
            with open(self.path, mode='w', encoding='UTF-8') as file:
                json.dump(self.init_data, file)
        else:
            with open(self.path, mode='r', encoding='UTF-8') as file:
                content = file.read().strip()
                if not content:
                    json.dump(self.init_data, file)

    def add_user(self, user):
        users = self._get_users()
        users.append(user)
        self._save_new_users(users)


# class SQLStorage:
#     def __init__(self):
#         self.cursor = ...
#         self.connection = ...

    # def add_user(self, user):
    #     self.cursor.execute(
    #         'INSERT INTO users(name, password) VALUES(%s, %s)',
    #         [user.get('name'), user.get('password')]
    #     )


class Authentication:
    def __init__(self):
        self.storage = JSONStorage()
        self.validation = Validation()

    def add_user(self, name, password):
        new_user = {'name': name, 'password': password}
        self.storage.add_user(new_user)


class Interaction:  # Bu bölümde ancaq inputlar alınır
    def __init__(self):
        pass

    def get_answer(self, message, accepted_list, exception):
        print(message)
        while True:
            user_inp = input("Click: ")
            if user_inp in accepted_list:
                return user_inp
            else:
                print(exception)

    def get_input(self, choice):
        if choice == "name":
            answer = "Name"

        elif choice == "surname":
            answer = "Surname"

        elif choice == "mail":
            answer = "Mail Address"

        elif choice == "pswd":
            answer = "Password"

        elif choice == "tel":
            answer = "Phone Number"

        elif choice == "key":
            answer = "Secret Key"

        return input("Enter your {}: ".format(answer))
            


class PasswordManager:
    def __init__(self):
        self.interaction = Interaction()

    def intro(self):
        intro_menu = """
        Welcome to Password Manager!

        '1' Sign in
        '2' Sign up
        '3' Restore Password
        '0' Exit
        """
        exception = "You made the wrong choice. Try again please!"
        accepted_list = list('0123')
        answer = self.interaction.get_answer(
            intro_menu, accepted_list, exception)

    def sign_up(self):
        self.validation = Validation()
        self.encyrption = Encryption()
        mail_false, pswd_false, key_false, name_false, surname_false, tel_false = False, False, False, False, False, False
        status = True
        while status:
            if not name_false:
                name = self.interaction.get_input(choice="name")
                if self.validation.validate_name(name):
                    name = name.capitalize()
                    hashed_name = self.encyrption.hashing(name)
                    name_false = True
            elif not surname_false:
                surname = self.interaction.get_input(choice="surname")
                if self.validation.validate_surname(surname):
                    surname = surname.capitalize()
                    hashed_surname = self.encyrption.hashing(surname)
                    surname_false = True
            elif not mail_false:
                mail = self.interaction.get_input(choice="mail")
                if self.validation.validate_mail(mail):
                    mail = mail.lower()
                    hashed_mail = self.encyrption.hashing(mail)
                    mail_false = True
            elif not pswd_false:
                pswd = self.interaction.get_input(choice="pswd")
                if self.validation.validate_password(pswd):
                    hashed_pswd = self.encyrption.hashing(pswd)
                    pswd_false = True
            elif not tel_false:
                tel = self.interaction.get_input(choice="tel")
                if self.validation.validate_phone(tel):
                    hashed_phone = self.encyrption.hashing(tel)
                    tel_false = True
            elif not key_false:
                key = self.interaction.get_input(choice="key")
                if self.validation.validate_key(key):
                    hashed_key = self.encyrption.hashing(key)
                    key_false = True