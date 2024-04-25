def is_prime_number():
    number = int(input("Введите натуральное число больше 1: "))
    if number <= 1:
        print("Число должно быть больше 1.")
        return

    divisor = 2
    while divisor < number:
        if number % divisor == 0:
            print(f"Число {number} не является простым, так как делится на {divisor}.")
            return
        divisor += 1

    print(f"Число {number} является простым.")

is_prime_number()
