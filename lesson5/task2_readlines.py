with open("task2_randomText", "r") as randText:
    lines = 0
    for line in randText.readlines():
        lines += 1
        words = 0
        for word in line.split():
            words += 1
        print(f"{lines} line has {words} word(s)")
    print(f"File \"{randText.name}\" has {lines} line(s)")
