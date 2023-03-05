def validate_mail(mail):
    if not "@" in mail[-14:-7] or not "." in mail[-6:-1]:
        # pattern = r'^[a-zA-Z0-9_][a-zA-Z0-9._%+-]*@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
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
    if not 3 < len(key) < 15 and ' ' in key:
        print("Security word lenght has to be min 3, max 15 characters! And spaces not acceptable!")
        return False
    else:
        return True

def validate_ns(name, surname):
    if not name.isalpha() or not surname.isalpha():
        print("Please reenter name and surname correctly!")
        return False
    else:
        return True


