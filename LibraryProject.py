#Register/Login
print("""
===================
1>     login

2>    register
===================
""")

n = int(input("Enter Number of Function: "))

# DEFAULT VALID CHECK
def validCheck(database, data, loginValid = False,):
    while loginValid != True:
        New = input(f"Enter your {data}: ")
        if New == "QUIT":
            return False
        elif not New or New.isspace() == True:
            print("You can't left it blank!")
            continue
        else:
            return New
            
# Log-in
if n == 1:
    Valid = False
    attempts = 4
    while Valid == False and attempts > 0:
        with open("Users.txt", "r") as file:
            print("Enter 'QUIT' if you want to leave.")
            input_login = input("Enter your login: ")
            input_password = input("Enter your password: ")
            for line in file:
                if ("Login:" + input_login + " Password:" + input_password) == line.strip():
                    print("You successfully log-in.")
                    print(f"\tWelcome {input_login}!")
                    Valid = True
            if Valid == True:
                break
            else:
                attempts -= 1
                print(f"Wrong login or password. You have {attempts} attempts left.")
                continue

        
# REGISTER LOGIN
if n == 2:
    Valid = False
    with open("Login.txt", "r") as file:
        exist_user = file.readlines()
        while Valid != True:
            NewLogin = validCheck(exist_user, "login")
            if NewLogin == False:
                exit()
            else:
                for line in exist_user:
                    if ("Login:" + NewLogin) == line.strip():
                        print("This login already using!")
                        break
                    else:
                        Valid = True
                        break
            continue
                    
# REGISTER PASSWORD
        Valid = False
        with open("Users.txt", "a") as file:
            while Valid != True:
                print("Enter 'QUIT' if you want to leave.")
                NewPassword = validCheck(exist_user, "password")
                file.write(f"\nLogin:{NewLogin} Password:{NewPassword}")
                with open("Login.txt", "a") as file:
                    file.write(f"\nLogin:{NewLogin}")
                Valid = True
                print("You successfully registered!")

else:
    exit()