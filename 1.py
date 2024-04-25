def count_divisible_by_three():
    count = 0
    while True:
        number = int(input("Введите число (0 для завершения): "))
        if number == 0:
            break
        if number % 3 == 0:
            count += 1
    print("Количество чисел, делящихся на 3:", count)

count_divisible_by_three()
