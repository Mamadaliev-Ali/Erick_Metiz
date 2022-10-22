#for value in range(1, 11):
  #  print(value)


num = list(range(1, 11, 2))
print(num)


numbers = []
for number in range(2, 11):
    numbers.append(number ** 3)
    print(numbers)


square = [val ** 2 for val in range(1, 11)]
print(square)