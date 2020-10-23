with open("task1_my_file.txt", "w") as my_file:
    txt = "1"
    while txt:
        txt = input("Your text: ")
        my_file.write(txt + "\n")
