responses = {}

# Установка флага
polling_active = True

while polling_active:
    # Запрос имени и ответа пользователя
    name = input("\nWhat is yor name")
    response = input("Which mountain would you like to climb someday? ")

    # Ответ сохроняется в словаре
    responses[name] = response

    # Проверка продолжения опроса
    repeat = input("Would you like to let another person respond? ( yes/ no)")
    if repeat == 'no':
        polling_active = False

print("\n ---Pool Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")

