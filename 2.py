def count_two_digit_ending_in_three():
    count = 0
    while True:
        number = int(input("Введите число (0 для завершения): "))
        if number == 0:
            break
        if 10 <= abs(number) <= 99 and number % 10 == 3:
            count += 1
    print("Количество двузначных чисел, заканчивающихся на 3:", count)

count_two_digit_ending_in_three()
