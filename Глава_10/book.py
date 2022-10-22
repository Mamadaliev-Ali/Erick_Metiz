fileName = 'book.txt'

with open(fileName, encoding='utf-8') as f:
    book = f.read()
    name = book.split().count('очень')

    print(name)
