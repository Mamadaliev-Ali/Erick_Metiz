while True:
    first_num = input("First numbers: ")
    if first_num == 'q':
        break
    second_num = input("Second number: ")
    if second_num == 'q':
        break
    try:
        division = int(first_num) * int(second_num)
    except ValueError:
        print("Enter a number")
    else:
        print(division)

        