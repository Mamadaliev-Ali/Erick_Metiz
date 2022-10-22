requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now")
    else:
        print(f"Adding {requested_topping}")

print("\nFinished making your pizza!")


toppings = []

if toppings:
    for topping in toppings:
        print(f"Adding {topping}")
        print("\nFinished miking your pizza")
    else:
        print("Are you sure you want a plain pizza")
