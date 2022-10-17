import hashlib
import ast


def main():

    intro()


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
            login()
            break
        elif user_inp == "2":
            add_user()
            break
        elif user_inp == "3":
            pass #restore_pswd()
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
    elif pswd.isupper() or pswd.islower():
        print("The password must include least 1 uppercase and 1 lowercase.")
        return False
    else:
        return True

def validate_num(number, select):
    if select=="1":
        lenght=10
    elif select == "2":
        lenght=9
    if not len(number)==lenght:
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

def validate_ns(name,surname):
    if not name.isalpha() or not surname.isalpha():
        print("Please reenter name and surname correctly!")
        return False
    else:
        return True

def add_user():
    email_correct = False
    pswd_correct = False
    key_correct = False
    name_correct = False
    numb_correct = False
    while True:
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
            code=0
            text_2="""
            Select your country from the menu below

            1- Turkey (+90)
            2- Azerbaijan (+994)
            """
            while True:
                print(text_2)
                select = input(": ")
                if select == "1":
                    code = "+90"
                    break
                elif select == "2":
                    code = "+994"
                    break
                else:
                    print("Plese select country code correctly!")

            number = input(f"Enter your phone number without leading '0': {code} ")
            if validate_num(number, select):
                nmbr = code+number
                numb_correct = True

        else:
            source = input("Platform name where the user is used: ").capitalize()

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
            result_dict = {}
            result_dict["source"] = source
            result_dict["first name"] = first_name
            result_dict["last name"] = last_name
            result_dict["number"] = nmbr_hash
            result_dict["mail"] = mail_hash
            result_dict["password"] = pswd_hash
            result_dict["key"] = key_hash
            f = open("passwords.txt", "a")
            f.write(str(result_dict)+"\n")
            f.close()
            print("Welcome", first_name, last_name,
                  "\nSing Up succesfully ended")
            intt = input("Enter to 'Y' go to main menu, 'Q' to exit...")
            if intt.lower() == "y":
                intro()
            else:
                break
            break


def login():
    while True:
        mail_int = input("Your mail: ")
        pswd_int = input("Your password: ")
        if validate_mail(mail_int) and validate_pswd(pswd_int):

            encval_mail = mail_int.encode()
            encval_pswd = pswd_int.encode()

            login_mail = hashlib.sha512(encval_mail).hexdigest()
            login_pswd = hashlib.sha512(encval_pswd).hexdigest()

            try:
                with open('passwords.txt', 'r') as r:
                    lines = r.readlines()
                    for line in lines:
                        user = ast.literal_eval(line.strip())
                        if login_mail == user["hashed mail"] and login_pswd == user["hashed password"]:
                            current_user = user
                            print("Login Succesfully ended\n\nWeolcome {} {}".format(user["first name"],user["last name"]))
                            logged_in(current_user, mail_int, pswd_int)
                            break
                        else:
                            sec = input(
                                "Mail or Password is not correct!\n1- try again,\n2- Restore Password\n3- Sing up,\nq- Exit\n__:")
                            if sec == "1":
                                login()
                            elif sec == "2":
                                restore_pswd()
                            elif sec == "3":
                                add_user()
                            else:
                                break
            except FileNotFoundError:
                print("User not found")


def logged_in(current_user, mail, pswd):
    input("bilgileri göstermek için Enter'e basınız: ")
    print("""
    Full name {} {},
    Mail Address: {},
    Your current password: {},
    Platform name: {}
    """.format(current_user["first name"], current_user["last name"], mail, pswd, current_user["source"]))


main()
