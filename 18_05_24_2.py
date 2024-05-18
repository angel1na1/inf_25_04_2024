# Дано натуральное число N. Получите число, полученное перестановкой цифр исходного числа в обратном порядке.
# Выведите на экран новое число и разность между исходным числом и преобразованным

N = int(input("Введите натуральное число N: "))

reversed_num = 0
original_num = N

while N > 0:
    last_digit = N % 10
    reversed_num = reversed_num * 10 + last_digit
    N = N // 10

difference = original_num - reversed_num

print("Новое число:", reversed_num)
print("Разность между исходным и новым числом:", difference)