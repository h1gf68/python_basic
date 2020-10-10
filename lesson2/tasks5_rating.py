rating = [8, 7, 5, 4, 2, 2]
while True:
    print(rating)
    newRating = input("Введите новый элемент рейтинга: ")

    # проверка введенного значения на пустую строку и является целым числом
    if not newRating or not newRating.isdigit():
        break

    newRating = int(newRating)

    if newRating > rating[0]:
        rating.insert(0, newRating)
    elif newRating < rating[-1]:
        rating.append(newRating)
    else:
        for num in range(len(rating)):
            if rating[num] >= newRating > rating[num + 1]:
                rating.insert(num + 1, newRating)
                break
