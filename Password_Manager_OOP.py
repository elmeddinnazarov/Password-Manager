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
        "^\+(?P<country>\d{1,3})-(?P<prefix>\d{2,3})-(?P<number>\d{3}-\d{2}-\d{2})$")
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

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

class Encryption:
    def __init__(self):
        pass

    def hashing(self, value):
        return str(hashlib.sha512(value.encode()).hexdigest())

    def encyrpt(self, value):
        import random
        import string
        import textwrap

        output = textwrap.wrap(value, 1)
        len_output = len(output)
        len_len_output = len(str(len_output))
        index = int(119/len_output)
        aralık = index
        len_aralık = len(str(aralık))
        letters = string.ascii_letters + string.digits +string.digits +string.punctuation
        random_str = ''.join(random.choice(letters) for i in range(120))
        for newstring in output: 
            random_str = random_str[:index] + newstring + random_str[index + 1:]
            index += aralık
        random_str = str(len_output).rjust(2,"&") + str(random_str)[10] + str(len_len_output) + str(random_str) + str(aralık).rjust(2,"%") + str(random_str)[10] + str(len_aralık)
        encyrpted_result = random_str
        return encyrpted_result

    def decyrpt(self, value):
        password = []
        first_part = value[:4]
        if not "&" in first_part:
            pw_lenght = first_part[:2]
        else:
            pw_lenght = first_part[1]
        pw_lenght = int(pw_lenght)
        second_part = value[-4:]
        if not "%" in second_part:
            pw_range = second_part[:2]
        else:
            pw_range = second_part[1]
        pw_range = int(pw_range)
        str_part = value[4:-4]
        st_range = pw_range
        for pw in range(pw_lenght):
            password.append(str_part[pw_range])
            pw_range+=st_range
        decyrpted_result = "".join(password)
        return decyrpted_result


#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------


class JSONStorage:
    users = []

    def __init__(self, filename='passwords.json'):
        self.path = Path(filename)
        self._initilize_file()
    
    def _save_new_users(self, new_users):
        new_content = {'users': new_users}
        with open(self.path, mode='w', encoding='UTF-8') as file:
            json.load(new_content, file)

    def _initilize_file(self):
        if not self.path.exists():
            with open(self.path, mode='w', encoding='UTF-8') as file:
                json.dump(self.users, file)
        else:
            with open(self.path, mode='r', encoding='UTF-8') as file:
                content = file.read().strip()
                if not content:
                    json.dump(self.users, file)

    def get_users(self):
        with open(self.path, mode='r', encoding='UTF-8') as file:
            content = json.load(file)
        return content.get('users')

    def add_user(self, user):
        users = self.get_users()
        users.append(user)
        self._save_new_users(users)


#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------


class SQLStorage:
    def __init__(self):
        self.cursor = ...
        self.connection = ...

    def add_user(self, user):
        self.cursor.execute(
            'INSERT INTO users(name, password) VALUES(%s, %s)',
            [user.get('name'), user.get('password')]
        )


#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------


class Authentication:
    def __init__(self):
        self.storage = JSONStorage()
        self.validation = Validation()

    def add_user(self, name, password):
        new_user = {'name': name, 'password': password}
        self.storage.add_user(new_user)


#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------


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

    def signup_input(self, choice):
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

        user_inp = input("Enter your {}: ".format(answer))
        return user_inp
            
    def wrong_attempt(self):
        text = """

        Something went wrong. The error can be caused by one of the following reasons.

        - User not found!
        - Mail or Password is not correct!

        '1' to try again,
        '2' to restore password,
        '3' to sign up,
        '0' to exit.


        """
        print(text)
        exception = "You made the wrong choice. Try again please!"
        accepted_list = list('0123')        
        while True:
            user_inp = input("> : ")
            if user_inp in accepted_list:
                return user_inp
            else:
                print(exception)

    
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------


class PasswordManager:
    def __init__(self):
        self.interaction = Interaction()
        self.validation = Validation()
        self.encyrption = Encryption()
        self.jsonStorage = JSONStorage()

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

        if answer == "1":
            pass
        elif answer == "2":
            self.sign_up()
        elif answer == "3":
            pass
        else:
            pass

    def execute(self):
        self.execute = self.intro

    def sign_up(self):
        mail_false, pswd_false, key_false, name_false, surname_false, tel_false = False, False, False, False, False, False
        user = {}
        status = True
        while status:
            if not name_false:
                name = self.interaction.signup_input(choice="name")
                if self.validation.validate_name(name):
                    name = name.capitalize()
                    user["name"] = self.encyrption.hashing(name)
                    name_false = True
            elif not surname_false:
                surname = self.interaction.signup_input(choice="surname")
                if self.validation.validate_surname(surname):
                    surname = surname.capitalize()
                    user["surname"] = self.encyrption.hashing(surname)
                    surname_false = True
            elif not mail_false:
                mail = self.interaction.signup_input(choice="mail")
                if self.validation.validate_mail(mail):
                    mail = mail.lower()
                    user["mail"] = self.encyrption.hashing(mail)
                    mail_false = True
            elif not pswd_false:
                pswd = self.interaction.signup_input(choice="pswd")
                if self.validation.validate_password(pswd):
                    user["password"] = self.encyrption.hashing(pswd)
                    pswd_false = True
            elif not tel_false:
                tel = self.interaction.signup_input(choice="tel")
                if self.validation.validate_phone(tel):
                    user["phone_number"] = self.encyrption.hashing(tel)
                    tel_false = True
            elif not key_false:
                key = self.interaction.signup_input(choice="key")
                if self.validation.validate_key(key):
                    user["secret_key"] = self.encyrption.hashing(key)
                    key_false = True
            status = False

        welcome_text = """

        Welcome {} {},
        Signup succesfully ended.

        Enter 'y' to go main manu, 'q' to exit...

        """.format(name, surname)
        exception = "You made the wrong choice. Try again please!"
        accepted_list = list('yqYQ')
        user_inp = self.interaction.get_answer(welcome_text, accepted_list, exception)
        self.jsonStorage.add_user(user)
        if user_inp.lower() == 'y':
            self.intro()
        else:
            print("Good Bye")

    def sign_in(self): # giriş edildikten sonra signed in fonksiyonuna yönlendirir
        mail_false, pswd_false = False, False
        status = True
        while status:
            if not mail_false:
                mail = self.interaction.signup_input(choice="mail")
                if self.validation.validate_mail(mail):
                    login_mail = self.encyrption.hashing(mail)
                    login_attept = False
                else:
                    print("Format not accepted!")

            elif not pswd_false:
                password = self.interaction.signup_input(choice="pswd")
                if self.validation.validate_password(password):
                    login_pswd = self.encyrption.hashing(password)
                    login_attept = False
                else:
                    print("Format not accepted!")

            for user in self.jsonStorage.get_users:
                if login_mail == user["mail"] and login_pswd == user["password"]:
                    current_user = user
                    login_attept = True
                    status = False
                    self.signed_in(current_user)
                    
            if login_attept == False:
                answer = self.interaction.wrong_attempt

                if answer == "0":
                    status = False # Programı sonlandır
                    break
                elif answer == "1":
                    continue # tekrar input al
                elif answer == "2":
                    self.sign_up # sign up' a yönlendir
                elif answer == "3":
                    self.restore_password # restore password'a yönlendir
                
    def restore_pswd(self):
        pass

    def signed_in(self):
        pass

    def change_main_mail(self):
        pass

    def change_main_pswd(self):
        pass

    def change_main_key(self):
        pass

    def user_interface(self):
        pass

    def platforms_menu(self):
        pass

    def list_all_platforms(self):
        pass

    def list_by_platform_name(self):
        pass

    def change_platform_info(self):
        pass

    def delete_platform(self):
        pass

    def restore_last_deletion(self):
        pass

password_manager = PasswordManager()

password_manager.execute()