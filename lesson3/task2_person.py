def person(**kwargs):
    myStr = ""
    for key, val in kwargs.items():
        myStr += f"{key} - {val}, "
    return myStr[:-2]


in_name = input("Имя: ")
in_surname = input("Фамилия: ")
in_birthYear = input("Год рождения: ")
in_city = input("Город проживания: ")
in_email = input("Адрес эл. почты: ")
in_phoneNumber = input("Номер телефона: ")

print(person(name=in_name, surname=in_surname, birthYear=in_birthYear, city=in_city, email=in_email,
             phoneNumber=in_phoneNumber))
