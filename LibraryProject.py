import os


#Register/Login
print("""
===================
1>     login

2>    register
===================
""")

n = int(input("Enter Number of Function: "))

# DEFAULT VALID CHECK
def validCheck(item, Valid = False,):
    while Valid != True:
        New = input(f"Enter your {item}: ")
        if New == "QUIT":
            return False
        elif not New or New.isspace() == True:
            print("You can't left it blank!")
            continue
        else:
            return New

# Search-Through-Entire-Library
def search(user_input, library):
    lines = ""
    for line in library:
        if user_input in line:
            lines = (f"{lines}\n{line}")
    if lines.isspace():
        return False
    else:
        return lines

def searchOne(user_input, library):
    lines = ""
    for line in library:
        if user_input in line:
            lines = (f"{lines}\n{line}")
            break
    if lines.isspace():
        return False
    else:
        return lines

# USER-FOLDER
def GetUserFolder():
    cwd = os.getcwd()
    UserFolder = os.path.join(cwd, "UsersInfo")
    UserFolder = os.path.join(UserFolder, f'{Login}.txt')
    return UserFolder


# Log-in
if n == 1:
    Valid = False
    attempts = 4
    while Valid == False and attempts > 0:
        print("Enter 'QUIT' if you want to leave.")
        Login = input("Enter your login: ")
        if Login == "QUIT":
            break
        input_password = input("Enter your password: ")
        if input_password == "QUIT":
            break
        try:
            with open(f"{GetUserFolder()}", "r", encoding="UTF-8") as file:
                for line in file:
                    if ("Login:" + Login + "Password:" + input_password) == line.strip():
                        print("You successfully log-in.")
                        print(f"\tWelcome {Login}!")
                        Valid = True
            if Valid == True:
                break
        except:
            attempts -= 1
            print(f"Wrong login or password. You have {attempts} attempts left.")
            continue
   
# Validate LOGIN
if n == 2:
    Valid = False
    while Valid == False:
        Login = validCheck("login")
        if Login == False:
            exit()
        else:
            try:
                with open(f"{GetUserFolder()}", "r") as file:
                    for line in file:
                        if f"{Login}.txt" in file:
                            print("This login already using!")
            except:
                pass
                    
# REGISTER ACCOUNT
        Valid = False
        while Valid == False:
            print("Enter 'QUIT' if you want to leave.")
            NewPassword = validCheck("password")

            cwd = os.getcwd()
            UserFolder = os.path.join(cwd, "UsersInfo")
            while not os.path.exists(UserFolder):
                os.mkdir(UserFolder)
                
            UserFolder = os.path.join(UserFolder, f'{Login}.txt')
            with open(UserFolder, "x") as info:
                info.write(f"Login:{Login}Password:{NewPassword}")
            Valid = True
            print("You successfully registered!")


if Valid == True:
    menu = True
    while menu:
        print(f"""
===========================
Welcome to Online Library!

Choose number of function!

1>         Store
                                
2>   Check Your Basket

3>         QUIT
===========================
""")

        n = (input())

        if n == '1':
            print("""
===========================
Choose number of function!

1>  Add Book to the Basket

2>  Book Search       
===========================
""")

            choose = input()
            inside = True
            while inside:
                if choose == "1":
                    with open("LibraryData.txt", "r", encoding="utf-8") as books:
                        print("If you don't know number of searching book go to 'Book Search' tab!")
                        print("Enter 'QUIT' if you want to go back.")
                        n = str(input("Enter Number of book: "))
                        if n == "QUIT":
                            inside = False
                        else:
                            add = searchOne(n, books)
                            Q = input(f"Do you want to add this book to your basket?\n{add}\nEnter: 'y' if Yes / any other answer will be considered as No\n")
                            if Q == "y":
                                with open(f"{GetUserFolder()}", "a", encoding="UTF-8") as basket:
                                    basket.write(f"{add}")
                                print(f"{add}\nSuccessfully added to your basket")
                            else:
                                continue
                            
                elif choose == "2":
                    with open("LibraryData.txt", "r", encoding="utf-8") as books:
                        print("Enter 'QUIT' if you want to go back.")
                        n = str(input("Enter Name or Author of book: "))
                        if n == "QUIT":
                            inside = False
                        else:
                            print(search(n, books))
                            continue
                            
        
        if n == "2":
            with open (f"{GetUserFolder()}", "r", encoding="utf_8") as basket:
                print(search(" ", basket))

        elif n == "3":
            break