def integer_square_root():
    n = int(input("Введите натуральное число: "))
    if n < 1:
        print("Число должно быть натуральным, то есть больше 0.")
        return

    root = 0
    while (root + 1) ** 2 <= n:
        root += 1

    print(f"Целый квадратный корень из {n} равен {root}")

integer_square_root()
