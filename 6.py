def multiply_using_addition():
    a = int(input("Введите первое целое число: "))
    b = int(input("Введите второе целое число: "))

    # Переменная для хранения результата
    result = 0

    # Учесть отрицательные числа, сохраняя знак
    positive_a = abs(a)
    positive_b = abs(b)

    # Основной цикл для добавления числа a, b раз
    for _ in range(positive_b):
        result += positive_a

    # Корректировка результата на основе знаков a и b
    if (a < 0 and b > 0) or (a > 0 and b < 0):
        result = -result

    print(f"Произведение чисел {a} и {b} равно {result}")

multiply_using_addition()
