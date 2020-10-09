number = input("Введите число из 2 или более цифр: ")
count = 1
max = int(number[0])
while count < len(number):
    if int(number[count]) > max:
        max = int(number[count])
    count += 1
print("Самая большая цифра в числе {} это: {} ".format(number, str(max)))
