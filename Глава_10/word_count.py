def count_words(file_name):
    try:
        with open(file_name, encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        pass
    else:
        words = content.split()
        num_word = len(words)
        print(f"The file {file_name} has about {num_word} words")


fileName = 'learning_pithon.txt'
count_words(fileName)
