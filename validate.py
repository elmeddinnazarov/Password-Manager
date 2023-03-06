import re


# PATTERNS

email_pattern = re.compile("^[a-z0-9]+([._%+-][a-z0-9]+)?@[a-z0-9.]+\.[a-z]{2,}$")
number_pattern = re.compile("^\d{9,10}$")



# VALIDATE FUNCTIONS

def validate_mail(mail):
    if not email_pattern.search(mail):
        print("Mail format not accepted!")
        return False
    else:
        return True

def validate_pswd(pswd):
    if len(pswd) < 8 or not re.search(r"[A-z]+", pswd) or not re.search(r"\d", pswd) or pswd.islower() or pswd.isupper():
        print(
            "At least 8 character please!\n"
            "Password must contain at least 1 letter or 1 number\n"  
            "The password must include least 1 uppercase and 1 lowercase.\n"
            )
        return False
    else:
        return True
    
def validate_num(number):
    if not number_pattern.match(number):
        print(
            "Please enter your phone number carefully!\n"
            "Numbers can not contain letters! Please enter your phone number carefully!"
              )
        return False
    else:
        return True

def validate_key(key):
    if not 3 < len(key) < 15 or ' ' in key:
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


