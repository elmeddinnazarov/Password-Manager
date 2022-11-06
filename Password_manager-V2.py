import hashlib
import json


def intro():
    
    text = """
        Welcome to Password Manager!

        '1' Sign in
        '2' Sign up
        '3' Restore Password
        '0' Exit

    """
    print(text)
    while True:
        user_inp = input("Click: ")
        if user_inp == "1":
            sign_in()
            break
        elif user_inp == "2":
            sign_up()
            break
        elif user_inp == "3":
            restore_pswd()
            break
        elif user_inp == "0":
            break
        else:
            print("You made the wrong choice. Try again please!")

def validate_mail(mail):
    if not "@" in mail[-14:-7] or not "." in mail[-6:-1]:
        print("Mail format not accepted!")
        return False
    else:
        return True

def validate_pswd(pswd):
    if len(pswd) < 8:
        print("at least 8 character please!")
        return False
    elif pswd.isnumeric():
        print("The password must include least 2 letter, 1 uppercase and 1 lowercase.")
    elif pswd.isupper() or pswd.islower():
        print("The password must include least 1 uppercase and 1 lowercase.")
        return False
    else:
        return True

def validate_num(number, select):
    if select == "1":
        lenght = 10
    elif select == "2":
        lenght = 9
    if not len(number) == lenght:
        print("Please enter your phone number carefully!")
        return False
    elif not number.isnumeric():
        print("Numbers can not contain letters! Please enter your phone number carefully!")
        return False
    else:
        return True

def validate_key(key):
    if not 3 < len(key) < 10:
        print("Security word lenght has to be min 3, max 10 characters!")
        return False
    else:
        return True

def validate_ns(name, surname):
    if not name.isalpha() or not surname.isalpha():
        print("Please reenter name and surname correctly!")
        return False
    else:
        return True

def wrong_attempt():
    sec = input(
        "User not found or mail or password is not correct!\n1- try again,\n2- Restore Password\n3- Sing up,\nq- Exit\n__:")
    if sec == "1":
        sign_in()
    elif sec == "2":
        restore_pswd()
    elif sec == "3":
        sign_up()
    else:
        print("See you again!")

def restore_pswd():
    email_correct = False
    key_correct = False
    name_correct = False
    numb_correct = False
    status = True
    while status:
        if not email_correct:
            mail = input("Enter your mail address: ").lower()
            if validate_mail(mail):
                email_correct = True
        elif not key_correct:
            key = input("Enter your security word: ").lower()
            if validate_key(key):
                key_correct = True
        elif not name_correct:
            first_name = input("Enter your first name: ")
            last_name = input("Enter your last name: ")
            if validate_ns(first_name, last_name):
                first_name = first_name.capitalize()
                last_name = last_name.capitalize()
                name_correct = True
        elif not numb_correct:
            code = 0
            text_2 = """
            Select your country from the menu below

            1- Turkey (+90)
            2- Azerbaijan (+994)
            """
            status_phone = True
            while status_phone:
                print(text_2)
                select = input(": ")
                if select == "1":
                    code = "+90"
                    status_phone = False
                elif select == "2":
                    code = "+994"
                    status_phone = False
                else:
                    print("Plese select country code correctly!")
                    status_phone = True

            number = input(
                f"Enter your phone number without leading '0': {code} ")
            if validate_num(number, select):
                nmbr = code+number
                numb_correct = True
        else:

            encmail = mail.encode()
            mail_hash = hashlib.sha512(encmail).hexdigest()

            enckey = key.encode()
            key_hash = hashlib.sha512(enckey).hexdigest()

            encnmbr = nmbr.encode()
            nmbr_hash = hashlib.sha512(encnmbr).hexdigest()

            mail_hash = str(mail_hash)
            key_hash = str(key_hash)
            nmbr_hash = str(nmbr_hash)
            try:
                with open("passwords.json") as r:
                    big_dict=json.load(r)
                    users = big_dict["users"]

            except FileNotFoundError:
                wrong_attempt()
                status = False
            login_attempt = False
            for user in users:
                if mail_hash == user["mail"] and key_hash == user["key"] and nmbr_hash == user["number"] and first_name == user["first name"] and last_name == user["last name"]:
                    print("Verification Complated! \n\n")
                    pswd_correct = True
                    while pswd_correct:
                        new_key_1 = input(
                            "Please enter your new password: ")
                        new_key_2 = input(
                            "Enter your new password again: ")
                        if not new_key_1 == new_key_2:
                            print(
                                "passwords are not the same! Please enter again!")
                        else:
                            if validate_pswd(new_key_1):
                                pswd_correct = False
                                encpswd = new_key_1.encode()
                                new_pswd = hashlib.sha512(encpswd).hexdigest()

                                user["password"] = new_pswd
                                big_dict["users"] = users
                                json.dumps(big_dict, indent=4)

                                with open("passwords.json", "w") as r:
                                    json.dump(big_dict, r)
                                input("Password successfully changed! Click 'Enter' to Main Menu: ")
                                intro()
                    login_attempt = True
            if login_attempt == False:
                wrong_attempt()
                status = False


def encyrption(input_value):
    import random
    import string
    import textwrap

    # global result
    output = textwrap.wrap(input_value, 1)
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
    result = random_str
    return result

def decyrption(result):
    # global user_pw
    password = []
    first_part = result[:4]
    if not "&" in first_part:
        pw_lenght = first_part[:2]
    else:
        pw_lenght = first_part[1]
    pw_lenght = int(pw_lenght)
    second_part = result[-4:]
    if not "%" in second_part:
        pw_range = second_part[:2]
    else:
        pw_range = second_part[1]
    pw_range = int(pw_range)
    str_part = result[4:-4]
    st_range = pw_range
    for pw in range(pw_lenght):
        password.append(str_part[pw_range])
        pw_range+=st_range
    user_pw = "".join(password)
    return user_pw

def sign_up():
    email_correct = False
    pswd_correct = False
    key_correct = False
    name_correct = False
    numb_correct = False
    status_signup = True
    while status_signup:
        if not email_correct:
            mail = input("Enter your mail address: ").lower()
            if validate_mail(mail):
                email_correct = True
        elif not pswd_correct:
            pswd = input("Enter your password: ")
            if validate_pswd(pswd):
                pswd_correct = True
        elif not key_correct:
            key = input("Enter your security word: ").lower()
            if validate_key(key):
                key_correct = True
        elif not name_correct:
            first_name = input("Enter your first name: ")
            last_name = input("Enter your last name: ")
            if validate_ns(first_name, last_name):
                first_name = first_name.capitalize()
                last_name = last_name.capitalize()
                name_correct = True
        elif not numb_correct:
            code = 0
            text_2 = """
            Select your country from the menu below

            1- Turkey (+90)
            2- Azerbaijan (+994)
            """
            status_phone = True
            while status_phone:
                print(text_2)
                select = input(": ")
                if select == "1":
                    code = "+90"
                    status_phone = False
                elif select == "2":
                    code = "+994"
                    status_phone = False
                else:
                    print("Plese select country code correctly!")

            number = input(
                f"Enter your phone number without leading '0': {code} ")
            if validate_num(number, select):
                nmbr = code+number
                numb_correct = True

        else:
            encpswd = pswd.encode()
            pswd_hash = hashlib.sha512(encpswd).hexdigest()

            encmail = mail.encode()
            mail_hash = hashlib.sha512(encmail).hexdigest()

            enckey = key.encode()
            key_hash = hashlib.sha512(enckey).hexdigest()

            encnmbr = nmbr.encode()
            nmbr_hash = hashlib.sha512(encnmbr).hexdigest()

            mail_hash = str(mail_hash)
            pswd_hash = str(pswd_hash)
            key_hash = str(key_hash)
            nmbr_hash = str(nmbr_hash)

            try:
                with open('passwords.json') as r:
                    big_dict = json.load(r)
                    users = big_dict["users"]
            except FileNotFoundError:
                big_dict = {}
                users = []

            user = {}
            user["first name"] = first_name
            user["last name"] = last_name
            user["number"] = nmbr_hash
            user["mail"] = mail_hash
            user["password"] = pswd_hash
            user["key"] = key_hash

            users.append(user)
            big_dict["users"] = users
            json.dumps(big_dict, indent=4)

            with open("passwords.json", "w") as r:
                json.dump(big_dict, r)

            print("Welcome", first_name, last_name,
                  "\nSing Up succesfully ended")
            intt = input("Enter to 'Y' go to main menu, 'Q' to exit...")
            if intt.lower() == "y":
                intro()
                status_signup = False
            else:
                status_signup = False

def sign_in():
    status_signin = True
    while status_signin:
        mail_int = input("Your mail: ")
        pswd_int = input("Your password: ")
        if validate_mail(mail_int) and validate_pswd(pswd_int):

            encval_mail = mail_int.encode()
            encval_pswd = pswd_int.encode()

            login_mail = hashlib.sha512(encval_mail).hexdigest()
            login_pswd = hashlib.sha512(encval_pswd).hexdigest()

            try:
                with open("passwords.json") as r:
                    big_dict = json.load(r)
                    users = big_dict["users"]
            except FileNotFoundError:
                wrong_attempt()
            login_attempt = False
            for user in users:
                if login_mail == user["mail"] and login_pswd == user["password"]:
                    current_user = user
                    signed_in(current_user, big_dict)
                    login_attempt = True
                    break
            if login_attempt == False:
                wrong_attempt()
                status_signin = False




def signed_in(current_user, big_dict):
    sign_int = input("""
    Welcome back {} {},
    
    1- Platforms,
    2- Change Account's Password,
    3- Change Account's Mail,
    4- Change Account's Secret Key,
    5- Log out,
    q- Exit

    : """.format(current_user["first name"], current_user["last name"]))

    if sign_int == "1":
        user_platforms(current_user, big_dict)
    elif sign_int == "2":
        account_pswd_change(current_user)
    elif sign_int == "3":
        account_mail_change(current_user)
    elif sign_int == "4":
        account_key_change(current_user)
    elif sign_int == "5":
        intro()
    else:
        pass

def account_pswd_change(current_user):
            try:
                with open("passwords.json") as r:
                    big_dict=json.load(r)
                    users = big_dict["users"]
            except FileNotFoundError:
                wrong_attempt()
            for user in users:
                    pswd_correct = True
                    while pswd_correct:
                        new_key_1 = input(
                            "Please enter your new password: ")
                        new_key_2 = input(
                            "Enter your new password again: ")
                        if not new_key_1 == new_key_2:
                            print(
                                "passwords are not the same! Please enter again!")
                        else:
                            if validate_pswd(new_key_1):
                                pswd_correct = False
                                encpswd = new_key_1.encode()
                                new_pswd = hashlib.sha512(encpswd).hexdigest()

                                user["password"] = new_pswd
                                big_dict["users"] = users
                                json.dumps(big_dict, indent=4)

                                with open("passwords.json", "w") as r:
                                    json.dump(big_dict, r)
                                input("Password successfully changed! Click 'Enter' to Account Menu: ")
                                signed_in(current_user)
                    else:
                        wrong_attempt()

def account_mail_change(current_user):
    try:
        with open("passwords.json") as r:
            big_dict=json.load(r)
            users = big_dict["users"]
    except FileNotFoundError:
        wrong_attempt()
    for user in users:
            mail_correct = True
            while mail_correct:
                new_key_1 = input(
                    "Please enter your new Mail Address: ")
                new_key_2 = input(
                    "Enter your Mail Address again: ")
                if not new_key_1 == new_key_2:
                    print(
                        "Mail Addresses are not the same! Please enter again!")
                else:
                    if validate_mail(new_key_1):
                        mail_correct = False
                        encpswd = new_key_1.encode()
                        new_mail = hashlib.sha512(encpswd).hexdigest()

                        user["mail"] = new_mail
                        big_dict["users"] = users
                        json.dumps(big_dict, indent=4)

                        with open("passwords.json", "w") as r:
                            json.dump(big_dict, r)
                        input("Mail Address successfully changed! Click 'Enter' to Account Menu: ")
                        signed_in(current_user)
            else:
                wrong_attempt()

def account_key_change(current_user):
    try:
        with open("passwords.json") as r:
            big_dict=json.load(r)
            users = big_dict["users"]
    except FileNotFoundError:
        wrong_attempt()
    for user in users:
            key_correct = True
            while key_correct:
                new_key_1 = input(
                    "Please enter your new Secret Key: ")
                new_key_2 = input(
                    "Enter your Secret Key again: ")
                if not new_key_1 == new_key_2:
                    print(
                        "Secret Keys are not the same! Please enter again!")
                else:
                    if validate_key(new_key_1):
                        key_correct = False
                        encpswd = new_key_1.encode()
                        new_key = hashlib.sha512(encpswd).hexdigest()

                        user["mail"] = new_key
                        big_dict["users"] = users
                        json.dumps(big_dict, indent=4)

                        with open("passwords.json", "w") as r:
                            json.dump(big_dict, r)
                        input("Secret Key successfully changed! Click 'Enter' to Account Menu: ")
                        signed_in(current_user)
            else:
                wrong_attempt()

def user_platforms(current_user, big_dict):
    pl_int = input("""
    
    1- Show Platforms,
    2- Add New Platform,
    3- Change Platform Information,
    4- Delete Platform,
    5- Log out,
    6- Back Menu,
    q- Exit

    : """)

    if pl_int == "1":
        show_platforms(current_user, big_dict)
    elif pl_int == "2":
        add_platform(current_user, big_dict)
    elif pl_int == "3":
        change_pl_info(current_user, big_dict)
    elif pl_int == "4":
        delete_platform(current_user, big_dict)
    elif pl_int == "5":
        intro()
    elif pl_int == "6":
        signed_in(current_user)
    else:
        "q a basılanda sign in e gedir. ne yazılmalıdır ki getmesin "

def show_platforms(current_user, big_dict):
        pl_info = input("""
    
        1- List All Platforms,
        2- List by Platform name,
        3- Log out,
        4- Back Menu,
        q- Exit

        : """)

        if pl_info == "1":
            all_platforms(current_user)
        elif pl_info == "2":
            list_by_name(current_user)
        elif pl_info == "3":
            intro()
        elif pl_info == "4":
            user_platforms()
        else:
            pass

def all_platforms(current_user):
    with open("passwords.json") as r:
        big_dict = json.load(r)
        users = big_dict["users"]
        current_user

        try:
            platforms = current_user["platforms"]
            pl_exsist = True

            for platform in platforms:
                print("""
                Platform Name: {}
                Mail Address: {}
                Username: {}
                Password: {}
                """.format(platform["pl_site"], decyrption(platform["pl_mail"]), decyrption(platform["pl_username"]), decyrption(platform["pl_pswd"])))

        except KeyError:
            pl_input = input("You did not add platform before! To add platform enter 'Y', 'Q' to exit!")
            if pl_input.isalpha and pl_input.lower() == "y":
                add_platform(current_user, big_dict)
                pl_exsist = False

        if pl_exsist:
            pass # platformları güzel bir formatta listeleyeceksın
                
def add_platform(current_user, big_dict):
    print("\nPlease enter the platform information you want to add!\n")
    pl_site = input("""Accepted Format: "facebook", "instagram" | Platform Name: """)
    pl_username = input("Username: ")
    pl_mail = input("Mail Address: ")
    pl_pswd = input("Password: ")

    pl_username = encyrption(pl_username)
    pl_mail = encyrption(pl_mail)
    pl_pswd = encyrption(pl_pswd)

    try:
        platforms = current_user["platforms"]
    except KeyError:
        platforms = []
    
    platform = {}
    platform["pl_site"] = pl_site
    platform["pl_username"] = pl_username
    platform["pl_mail"] = pl_mail
    platform["pl_pswd"] = pl_pswd
    platforms.append(platform)
    current_user["platforms"] = platforms
    
    with open("passwords.json", "w") as r:
        json.dump(big_dict, r)
    
    print("\nPlatform added successfully.\n")
    user_platforms(current_user, big_dict)

# def list_by_name(current_user):
#     pl_name = input("Write Platform Name to show information: ")
#     with open("passwords.json") as r:
#         big_dict = json.load(r)
#         users = big_dict["users"]
#         current_user

#         try:
#             platforms = current_user["platforms"]
#             print(platform)

# Hele bu bölüm hazır deyilş hazır olanda push eliyecem xeber eliyecem sene


#             for platform in platforms:
#                 if platform == pl_name:
#                     print("""
#                     Platform Name: {}
#                     Mail Address: {}
#                     Username: {}
#                     Password: {}
#                     """.format(platform["pl_site"], decyrption(platform["pl_mail"]), decyrption(platform["pl_username"]), decyrption(platform["pl_pswd"])))

        except KeyError:
            pl_input = input("You did not add platform before! To add platform enter 'Y', 'Q' to exit!")
            if pl_input.isalpha and pl_input.lower() == "y":
                add_platform(current_user, big_dict)


intro()