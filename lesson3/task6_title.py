def int_func(val):
    for i in val:
        if not (ord("a") <= ord(i) <= ord("z")):
            return
    return str(val[:1]).upper() + str(val[1:])


inputStr = input("Введите слова из латинских букв в нижнем регистре, разделенных пробелом: ")

outputStr = ""
for word in inputStr.split():
    if type(int_func(word)) == str:
        outputStr += int_func(word) + " "

print(outputStr)
