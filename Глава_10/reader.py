import json


userName = input('What is your name? ')

file_name = 'files/user_name.json'
with open(file_name, 'a') as f:
    json.dump(userName, f)
