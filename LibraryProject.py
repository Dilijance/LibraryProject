#Register/Login
print("""
===================
1>     login

2>    register
===================
""")

n = int(input("Enter Number of Function: "))

# DEFAULT VALID CHECK
def validCheck(item, loginValid = False,):
    while loginValid != True:
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
            lines = (f"{lines}\t{line}")
    if lines.isspace():
        return False
    else:
        return lines

def searchOne(user_input, library):
    lines = ""
    for line in library:
        if user_input in line:
            lines = (f"{lines}\t{line}")
            break
    if lines.isspace():
        return False
    else:
        return lines



# Log-in
if n == 1:
    Valid = False
    attempts = 4
    while Valid == False and attempts > 0:
        with open("Users.txt", "r") as file:
            print("Enter 'QUIT' if you want to leave.")
            input_login = input("Enter your login: ")
            if input_login == "QUIT":
                break
            input_password = input("Enter your password: ")
            if input_password == "QUIT":
                break
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
        while Valid != True:
            NewLogin = validCheck("login")
            if NewLogin == False:
                exit()
            else:
                for line in file:
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
                NewPassword = validCheck("password")
                file.write(f"\nLogin:{NewLogin} Password:{NewPassword}")
                with open("Login.txt", "a") as file:
                    file.write(f"\nLogin:{NewLogin}")
                Valid = True
                print("You successfully registered!")



if Valid == True:
    menu = True
    while menu:
        print(f"""
        ===========================
        Welcome       {input_login or NewLogin}!

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
            ===========================""")

            choose = input()
            inside = True
            while inside:
                if choose == "1":
                    with open("LibraryData.txt", "r", encoding="utf-8") as books:
                        print("If you don't know number of searching book go to 'Book Search' tab!")
                        print("Enter 'QUIT' if you want to go back.")
                        n = str(input("Enter Number of book: "))
                        if n == "QUIT":
                            break
                        else:
                            add = searchOne(n, books)
                            Q = input(f"Do you want to add this book to your basket?\n{add}\nEnter: 'y' if Yes / any other answer will be considered as No")
                            if Q == "y":
                                with open("Basket.txt", "a", encoding="UTF-8") as basket:
                                    basket.write(f"\n{add}")
                                print(f"{add}\nSuccessfully added to your basket")
                            else:
                                continue
                            



                elif choose == "2":
                    with open("LibraryData.txt", "r", encoding="utf-8") as books:
                        print("Enter 'QUIT' if you want to go back.")
                        n = str(input("Enter Name or Author of book: "))
                        if n == "QUIT":
                            break
                        else:
                            lines = search(n, books)
                            print(lines)
                            searching = True
                            while searching:
                                print("Enter 'QUIT' if you want to go to back.")
                                print("Searching through this books.")
                                n = input()
                                if n == "QUIT":
                                    break
                                else:
                                    lines = search(n, lines)
                                    if lines == False:
                                        print("There is no such book.")
                                        continue
                                    else:
                                        print(lines)
                                        break
        
        # if n == "2":
        #     with
        #     for number in basket:

        #     continue



