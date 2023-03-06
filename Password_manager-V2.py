import hashlib
import json
import validate as val
import encyrption as enc

def intro():
    
    text = """
        Welcome to Password Manager!

        '1' Sign in
        '2' Sign up
        '3' Restore Password
        '0' Exit

    """
    print(text)
    status = True
    while status:
        user_inp = input("Click: ")
        if user_inp == "1":
            status = False
            sign_in()
        elif user_inp == "2":
            status = False
            sign_up()
        elif user_inp == "3":
            status = False
            restore_pswd()
        elif user_inp == "0":
            status = False
        else:
            print("You made the wrong choice. Try again please!")


def restore_pswd():
    email_correct = False
    key_correct = False
    name_correct = False
    numb_correct = False
    status = True
    while status:
        if not email_correct:
            mail = input("Enter your mail address: ").lower()
            if val.validate_mail(mail):
                email_correct = True
        elif not key_correct:
            key = input("Enter your security word: ").lower()
            if val.validate_key(key):
                key_correct = True
        elif not name_correct:
            first_name = input("Enter your first name: ")
            last_name = input("Enter your last name: ")
            if val.validate_ns(first_name, last_name):
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
            if val.validate_num(number, select):
                nmbr = code+number
                numb_correct = True
        else:

            mail_hash = str(hashlib.sha512(mail.encode()).hexdigest())
            key_hash = str(hashlib.sha512(key.encode()).hexdigest())
            nmbr_hash = str(hashlib.sha512(nmbr.encode()).hexdigest())

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
                            if val.validate_pswd(new_key_1):
                                pswd_correct = False
                                new_pswd = hashlib.sha512(new_key_1.encode()).hexdigest()

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



def wrong_attempt():
    print(
        "User not found or mail or password is not correct!\n\t1- try again,\n\t2- Restore Password\n\t3- Sing up,\n\t0- Exit\n\t__:")
    status = True
    while status:
        user_inp = input("Click: ")
        if user_inp == "1":
            sign_in()
        elif user_inp == "2":
            status = False
            sign_up()
        elif user_inp == "3":
            status = False
            restore_pswd()
        elif user_inp == "0":
            status = False
        else:
            print("You made the wrong choice. Try again please!")

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
            if val.validate_mail(mail):
                email_correct = True
        elif not pswd_correct:
            pswd = input("Enter your password: ")
            if val.validate_pswd(pswd):
                pswd_correct = True
        elif not key_correct:
            key = input("Enter your security word: ").lower()
            if val.validate_key(key):
                key_correct = True
        elif not name_correct:
            first_name = input("Enter your first name: ")
            last_name = input("Enter your last name: ")
            if val.validate_ns(first_name, last_name):
                first_name = first_name.capitalize()
                last_name = last_name.capitalize()
                name_correct = True
        elif not numb_correct:
            country_menu = """
            Select your country from the menu below

            1- Turkey (+90)
            2- Azerbaijan (+994)
            """
            status_phone = True
            while status_phone:
                print(country_menu)
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
            if val.validate_num(number, select):
                full_num = code+number
                numb_correct = True

        else:
            pswd_hash = str(hashlib.sha512(pswd.encode()).hexdigest())
            mail_hash = str(hashlib.sha512(mail.encode()).hexdigest())
            key_hash = str(hashlib.sha512(key.encode()).hexdigest())
            nmbr_hash = str(hashlib.sha512(full_num.encode()).hexdigest())

            try:
                with open('passwords.json') as r:
                    big_dict = json.load(r)
                    users = big_dict["users"]
            except FileNotFoundError:
                big_dict = {}
                users = []

            user = {
                "first name": first_name,
                "last name": last_name,
                "number": nmbr_hash,
                "mail": mail_hash,
                "password": pswd_hash,
                "key": key_hash
            }
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
            else:
                status_signup = False

def sign_in():
    status_signin = True
    while status_signin:
        mail_int = input("Your mail: ")
        pswd_int = input("Your password: ")
        if val.validate_mail(mail_int) and val.validate_pswd(pswd_int):
            mail_int = mail_int.lower()
            login_mail = hashlib.sha512(mail_int.encode()).hexdigest()
            login_pswd = hashlib.sha512(pswd_int.encode()).hexdigest()

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
                status_signin = False
                wrong_attempt()

def signed_in(current_user, big_dict):
    status_signed = True
    while status_signed:
        usr_ans = input("""
        Welcome back {} {},
        
        1- Platforms,
        2- Change Account's Password,
        3- Change Account's Mail,
        4- Change Account's Secret Key,
        5- Log out,
        q- Exit

        : """.format(current_user["first name"], current_user["last name"]))

        if usr_ans == "1":
            user_platforms(current_user, big_dict)
        elif usr_ans == "2":
            account_pswd_change(current_user, big_dict)
        elif usr_ans == "3":
            account_mail_change(current_user, big_dict)
        elif usr_ans == "4":
            account_key_change(current_user, big_dict)
        elif usr_ans == "5":
            intro()
        elif usr_ans.lower() == "q":
            status_signed = False
        else:
            print("\nYou made the wrong choice!")

def account_pswd_change(current_user, big_dict):
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
            if val.validate_pswd(new_key_1):
                pswd_correct = False
                
    encpswd = new_key_1.encode()
    new_pswd = hashlib.sha512(encpswd).hexdigest()
    if current_user in big_dict["users"]:
        current_user["password"] = new_pswd
    else:
        print("bilinmeyen hata")
    json.dumps(big_dict, indent=4)
    with open("passwords.json", "w") as r:
        json.dump(big_dict, r)
    input("Password successfully changed! Click 'Enter' to Account Menu: ")
    signed_in(current_user, big_dict)

def account_mail_change(current_user, big_dict):
    mail_correct = True
    while mail_correct:
        new_mail_1 = input(
            "Please enter your new mail: ")
        new_mail_2 = input(
            "Enter your new mail again: ")
        if not new_mail_1 == new_mail_2:
            print(
                "Mails are not the same! Please enter again!")
        else:
            if val.validate_mail(new_mail_1):
                mail_correct = False
                
    encmail = new_mail_1.encode()
    new_mail = hashlib.sha512(encmail).hexdigest()
    if current_user in big_dict["users"]:
        current_user["mail"] = new_mail

    json.dumps(big_dict, indent=4)
    with open("passwords.json", "w") as r:
        json.dump(big_dict, r)
    input("Mail successfully changed! Click 'Enter' to Account Menu: ")
    signed_in(current_user, big_dict)

def account_key_change(current_user, big_dict):
    key_correct = True
    while key_correct:
        new_key_1 = input(
            "Please enter your new Secret Key: ")
        new_key_2 = input(
            "Enter your new Secret Key again: ")
        if not new_key_1 == new_key_2:
            print(
                "Secret Key are not the same! Please enter again!")
        else:
            if val.validate_key(new_key_1):
                key_correct = False
                
    enckey = new_key_1.encode()
    new_key = hashlib.sha512(enckey).hexdigest()
    if current_user in big_dict["users"]:
        current_user["key"] = new_key

    json.dumps(big_dict, indent=4)
    with open("passwords.json", "w") as r:
        json.dump(big_dict, r)
    input("Secret Key successfully changed! Click 'Enter' to Account Menu: ")
    signed_in(current_user, big_dict)

def user_platforms(current_user, big_dict):
    try:
        platforms = current_user["platforms"]
        status = True
    except KeyError:
        m_inp = input("You did not add any platform before!\n\nto add platform enter '1',\nto main menu click enter.\n\n    >...")
        if m_inp == "1":
            add_platform(current_user, big_dict)
        else:
            status = False
            signed_in(current_user, big_dict)

    while status:
        pl_int = input("""
        
        1- Show Platforms,
        2- Add New Platform,
        3- Change Platform Information,
        4- Delete Platform,
        7- Restore Last Deletion Process,
        5- Log out,
        6- Back Menu,
        q- Exit

        : """)
        if pl_int == "1":
            show_platforms(current_user, big_dict, platforms)
        elif pl_int == "2":
            add_platform(current_user, big_dict)
        elif pl_int == "3":
            change_platform_info(big_dict, platforms)
        elif pl_int == "4":
            rm_platform = delete_platform(current_user, big_dict, platforms)
        elif pl_int == "5":
            intro()
        elif pl_int == "6":
            signed_in(current_user, big_dict)
        elif pl_int == "7":
            try:
                restore_deletion(big_dict, platforms, rm_platform)
            except UnboundLocalError:
                print("\nThe system did not detect any previous deletion.")
        elif pl_int.lower() == "q":
            break
        else:
            print("\nYou made the wrong choice!")
            
def show_platforms(current_user, big_dict, platforms):
    while True:
        pl_info = input("""

        1- List All Platforms,
        2- List by Platform name,
        3- Log out,
        4- Back Menu,
        q- Exit

        : """)
        if pl_info == "1":
            all_platforms(platforms)
            show_platforms(current_user, big_dict, platforms)
        elif pl_info == "2":
            list_by_name(platforms)
            show_platforms(current_user, big_dict, platforms)
        elif pl_info == "3":
            intro()
        elif pl_info == "4":
            user_platforms(current_user, big_dict)
        elif pl_info.lower() == "q":
            break
        else:
            print("\nYou made the wrong choice!")

def all_platforms(platforms):
    for platform in platforms:
        print("""
        Platform Name: {}
        Mail Address: {}
        Username: {}
        Password: {}
        """.format(platform["pl_site"], enc.decyrption(platform["pl_mail"]), enc.decyrption(platform["pl_username"]), enc.decyrption(platform["pl_pswd"])))
    input("\n\nClick 'Enter' to Platform Menu: \n\n")
    

def list_by_name(platforms):
    pl_name = input("Write Platform Name: ")
    not_exist = True
    for platform in platforms:
        if platform["pl_site"] == pl_name:
            platform_name = platform["pl_site"]
            platform_mail = enc.decyrption(platform["pl_mail"])
            platform_password = enc.decyrption(platform["pl_pswd"])
            platform_username = enc.decyrption(platform["pl_username"])
            print("""
            Platform Name: {}
            Mail Address: {}
            Username: {}
            Password: {}
            """.format(platform_name, platform_mail, platform_username, platform_password))
            not_exist = False
            return platform_name, platform_username, platform_mail, platform_password
    if not_exist == True:
        print("The Platform Which is you search not exist!")

def add_platform(current_user, big_dict):
    print("\nPlease enter the platform information you want to add!\n")
    pl_site = input("""Accepted Format: "facebook", "instagram" | Platform Name: """)
    pl_username = input("Username: ")
    pl_mail = input("Mail Address: ")
    pl_pswd = input("Password: ")

    pl_username = enc.encyrption(pl_username)
    pl_mail = enc.encyrption(pl_mail)
    pl_pswd = enc.encyrption(pl_pswd)

    try:
        platforms = current_user["platforms"]
    except KeyError:
        platforms = []
    
    platform = {
        "pl_site": pl_site,
        "pl_username": pl_username,
        "pl_mail": pl_mail,
        "pl_pswd": pl_pswd
    }

    platforms.append(platform)
    current_user["platforms"] = platforms
    
    with open("passwords.json", "w") as r:
        json.dump(big_dict, r)
    
    print("\nPlatform added successfully.\n")
    user_platforms(current_user, big_dict)

def change_platform_info(big_dict, platforms):
    result = list_by_name(platforms)

    while True:
        ch_pl_info = input("""
        Whitch one you want to change ?
        Enter '1' to 'Username',
        Enter '2' to 'Mail Address',
        Enter '3' to 'Password'.

        You can choose more than one option like; '23' or '123'

        /...""")

        if not ch_pl_info.isnumeric() and not len(ch_pl_info) <=3:
            print("You made the wrong choice!")

        else:
            ch_pl_info = {*ch_pl_info}
            if "1" in ch_pl_info:
                username = input("New Username: ")
            if "2" in ch_pl_info:
                mail = input("New Mail Address: ")
            if "3" in ch_pl_info:
                password = input("New Password: ")

            for platform in platforms:
                if result[0] == platform["pl_site"]:
                    try:
                        platform["pl_username"] = enc.encyrption(username)
                    except NameError:
                        pass
                    try:
                        platform["pl_mail"] = enc.encyrption(mail)
                    except NameError:
                        pass
                    try:
                        platform["pl_pswd"] = enc.encyrption(password)
                    except NameError:
                        pass
            json_write(big_dict)
            break

def delete_platform(current_user, big_dict, platforms):
    print("Enter Platform Name which is you want to delete!\n")
    result = list_by_name(platforms)
    status = True
    while status:
        choice = input("The informations will be delete permanently. Are you sure to delete this platform? \n\nEnter 'C' to cancle, 'Y' to delete: ")
        if choice.lower() == "c":
            user_platforms(current_user, big_dict)
            status = False
        elif choice.lower() == "y":
            for platform in platforms:
                if result[0] == platform["pl_site"]:
                    platforms.remove(platform)
                    json_write(big_dict)
                    status = False
                    print("Platform has been removed!")
                    return platform
        else:
            print("You made the wrong choice!")

def restore_deletion(big_dict, platforms, removed_platform):
    input("Click Enter to contuniue restore last deletion process.\n    /... ")
    platforms.append(removed_platform)
    json_write(big_dict)
    print("\nRestore process complate succesfully!")

def json_write(value):
    json.dumps(value, indent=4)
    with open("passwords.json", "w") as file:
        json.dump(value, file)

def email_verificaion(email):
    import boto3

    AWS_ACCESS_KEY_ID = 'AKIAWGJBI35RRUTZTTGT'
    AWS_SECRET_ACCESS_KEY = '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'
    AWS_REGION = 'eu-north-1'

    client = boto3.client('ses',
                        aws_access_key_id=AWS_ACCESS_KEY_ID,
                        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                        region_name=AWS_REGION)


    response = client.send_email(
        Source='info.passwordmanager.com',
        Destination={
            'ToAddresses': [
                email
            ]
        },
        Message={
            'Subject': {
                'Data': 'Password Manager - Verify Your Account'
            },
            'Body': {
                'Text': {
                    'Data': "Your 6 digit verification code\n : 345673"
                }
            }
        }
    )


intro()