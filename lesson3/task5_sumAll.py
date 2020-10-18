def sum_list(numbers, start_sum):
    is_continue = True
    for num in numbers:
        if str(num).lower() == "q":
            is_continue = False
            break
        else:
            start_sum += float(num)
    return start_sum, is_continue


endSum = 0
while True:
    print("Для выхода из программы введите \"q\"")
    numList = input("Введите числа через пробел: ").split()
    endSum, isContinue = sum_list(numList, endSum)
    print(f"Общая сумма равна {endSum}")

    if not isContinue:
        print("Пойду отдохну!")
        break
