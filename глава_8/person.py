def build_person(first_name, last_name, age=None):
    """Возвращает словарь с информацией о человеке"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


name = build_person('jimi', 'hendrix', age=34)
print(name)