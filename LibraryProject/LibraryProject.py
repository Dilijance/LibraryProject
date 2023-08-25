#Register/Login
print("""
===================
1>     login

2>    register
===================
""")

n = int(input("Enter Number of Function: "))

# DEFAULT VALID CHECK
def validCheck(data, loginValid = False,):
    while loginValid != True:
        New = input(f"Enter your {data}: ")
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
        return "There is no such book."
    else:
        return lines


# Log-in
if n == 1:
    LoginValid = False
    attempts = 4
    while LoginValid == False and attempts > 0:
        with open("Users.txt", "r") as file:
            print("Enter 'QUIT' if you want to leave.")
            input_login = input("Enter your login: ")
            input_password = input("Enter your password: ")
            for line in file:
                if ("Login:" + input_login + " Password:" + input_password) == line.strip():
                    print("You successfully log-in.")
                    print(f"\tWelcome {input_login}!")
                    LoginValid = True
            if LoginValid == True:
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



if LoginValid == True:
    basket = []
    menu = True
    while menu:
        print(f"""
        ===========================
        Welcome       {input_login}!

        Choose number of function!

        1>         Store
                                
        2>   Check Your Basket

        3>         QUIT
        ===========================
        """)

        n = int(input())

        if n == 1:
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
                        print("Enter 'QUIT' if you want to go to back.")
                        n = str(input("Enter Number of book: "))
                        if n == "QUIT":
                            break
                        else:
                            add = search(n, books)
                            Q = input((f"Do you want to add this book to your basket?", "\n", add, "\n","Enter: 'y' if Yes / any other answer will be considered as No"))
                            if Q == "y":
                                basket.append(n)
                                print(f"{add}\nSuccessfully added to your basket")
                            else:
                                continue
                            



                elif choose == "2":
                    with open("LibraryData.txt", "r", encoding="utf-8") as books:
                        print("Enter 'QUIT' if you want to go to back.")
                        n = str(input("Enter Name or Author of book: "))
                        if n == "QUIT":
                            break
                        else:
                            searching = True
                            while searching:
                                lines = search(n, books)
                                print(lines)
                                print("Enter 'QUIT' if you want to go to back.")
                                print("Searching through this books.")
                                n = input()
                                if n == "QUIT":
                                    break
                                else:
                                    lines = search(n, lines)

