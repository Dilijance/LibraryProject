with open("LibraryData.txt", "r", encoding="utf-8") as library:
    lines = ""
    user_input = "Harry"
    for line in library:
        if user_input in line:
            lines = (f"{lines}\t{line}")
    print(lines)