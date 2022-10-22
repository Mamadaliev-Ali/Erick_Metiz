file_name = 'learning_pithon.txt'


try:
    with open(file_name) as f:
        content = f.read()
except FileNotFoundError:
    print('Not File')
else:
    words = content.split()
    num_word = len(words)
    print(num_word)






