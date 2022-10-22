import json


def get_stored_userName():
    """Получает хранимое имя пользователя"""
    fileName = 'userName.json'
    try:
        with open(fileName) as f:
            userName = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return userName


def get_new_userName():
    """Запрашивает новое имя пользователя"""
    userName = input("What's your name? ")
    fileName = 'userName.json'
    with open(fileName, 'w') as f:
        json.dump(userName, f)
    return userName


def great_user():
    """Приветствуем пользователя"""
    userName = get_stored_userName()
    if userName:
        print(f"Welcome back, {userName}")
    else:
        userName = get_new_userName()
        print(f"We'll remember you when you come back {userName}")


great_user()