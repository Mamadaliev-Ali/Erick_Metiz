import json

file_name = 'load.json'

with open(file_name) as f:
    """"чтение из файла с помощью json"""
    number = json.load(f)

    print(f"Я знаю ваше любимое число!Это{number}")
