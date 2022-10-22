file_name = '..\\learning_pithon.txt'
with open(file_name) as file_object:
    lines = file_object.read()


types = ''
for line in lines:
    types += line
    print(f"{types}")
    print(len(types))




