def find_max_even_number():
    max_even = None  # Используем None для идентификации отсутствия четных чисел
    while True:
        number = int(input("Введите число (0 для завершения): "))
        if number == 0:
            break
        if number % 2 == 0:
            if max_even is None or number > max_even:
                max_even = number

    if max_even is None:
        print("Четные числа не были введены.")
    else:
        print("Максимальное четное число:", max_even)

find_max_even_number()
