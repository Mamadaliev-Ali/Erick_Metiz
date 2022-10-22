file_name = 'work\\txt\\pi_digits.txt'
with open(file_name) as file_open:
    lines = file_open.readlines()


for line in lines:
    print(line.rstrip())