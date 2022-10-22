file_names = ['cats.txt', 'dogs.txt']

for file_name in file_names:
    try:
        with open(file_name) as f:
            pets = f.read()
    except FileNotFoundError:
        pass
    else:
        print(pets)
