alien = {'color': 'red', 'points': 4}
# print(alien['speed']) KeyError

value = alien.get('speed')
print(value)