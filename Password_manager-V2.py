import hashlib
import ast
def main():

    intro()

def intro():
    text="""
        Welcome to Password Manager!

        '1' Sign in
        '2' Sign up
        '0' Exit

    """
    print(text)
    while True:
        user_inp=input("Click: ")
        if user_inp=="2":
            add_user()
            break
        elif user_inp=="1":
            login()
            control_login()
            break
        elif user_inp=="0":
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
    if len(pswd) <8:                
        print("at least 8 character please!")
        return False
    elif pswd.isupper() or pswd.islower():
        print("The password must include least 1 uppercase and 1 lowercase.")
        return False
    else:
        return True

def validate_key(key):
    if not 3<len(key)<10:
        print("Security word lenght has to be min 3, max 10 characters!")
        return False
    else:
        return True

def add_user():
    email_correct=False
    pswd_correct=False
    key_correct=False
    while True:
        if not email_correct:
            mail=input("Enter your mail address: ").lower()
            if validate_mail(mail):
                email_correct=True
        elif not pswd_correct:
            pswd=input("Enter your password: ")
            if validate_pswd(pswd):
                pswd_correct=True
        elif not key_correct:
            key=input("Enter your security word: ").lower()
            if validate_key(key):
                key_correct=True
            
        else:
            first_name=input("Enter your first name: ").capitalize()
            last_name=input("Enter your last name: ").capitalize()
            source=input("Platform name where the user is used: ").capitalize()


            encpswd=pswd.encode()
            pswd_hash=hashlib.sha512(encpswd).hexdigest()

            encmail=mail.encode()
            mail_hash=hashlib.sha512(encmail).hexdigest()

            enckey=key.encode()
            key_hash=hashlib.sha512(enckey).hexdigest()

            mail_hash=str(mail_hash)
            pswd_hash=str(pswd_hash)
            key_hash=str(key_hash)
            result_dict={}
            result_dict["source"]=source
            result_dict["first name"]=first_name
            result_dict["last name"]=last_name
            result_dict["hashed mail"]=mail_hash
            result_dict["hashed password"]=pswd_hash
            result_dict["hashed key"]=key_hash
            f = open("passwords.txt", "a")
            f.write(str(result_dict)+"\n")
            f.close()
            print("Welcome",first_name,last_name,"\nSing Up succesfully ended")
            intt=input("Enter to 'Y' go to main menu, 'Q' to exit...")
            if intt.lower()=="y":
                intro()
            else:
                break
            break
  
def login():
    while True:
        mail_int=input("Your mail: ")
        pswd_int=input("Your password: ")
        if validate_mail(mail_int) and validate_pswd(pswd_int):

            encval_mail=mail_int.encode()
            encval_pswd=pswd_int.encode()

            login_mail=hashlib.sha512(encval_mail).hexdigest()
            login_pswd=hashlib.sha512(encval_pswd).hexdigest()

            try:
                with open('passwords.txt', 'r') as r:
                    lines=r.readlines()
                    for line in lines:
                        user=ast.literal_eval(line.strip())
                        if login_mail == user["hashed mail"] and login_pswd == user["hashed password"]:
                            print("giriş başarılı")
                            break
                        else:
                            sec = input("Mail or Password is not correct!\n1- try again,\n2- Sing up,\nq- Exit\n__:")
                            if sec == "1":
                                continue
                            elif sec == "2":
                                add_user()
                                break
                            elif sec.lower() == "q":
                                break
            except FileNotFoundError:
                print("Henüz Sisteme kullanıcı eklenmedi")
        break

def control_login():
    if login():
        print("you are logged in succesfully")
    else:
        print("Mail/Password is uncorrect")
        
main()
