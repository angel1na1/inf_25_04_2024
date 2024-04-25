def access_secret_information():
    correct_password = "1234"  # Здесь можно установить желаемый пароль
    while True:
        password_input = input("Введите пароль: ")
        if password_input == correct_password:
            break
        else:
            print("Неверный пароль, попробуйте снова.")

    # Основная часть программы
    print("Секретные сведения: 42 - ответ на главный вопрос жизни, вселенной и всего такого.")

access_secret_information()
