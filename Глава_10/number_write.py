import json

number = input("Введите число")

file_name = 'load.json'
"""Запись в файл через json"""
with open(file_name, 'w') as f:
    json.dump(number, f)


