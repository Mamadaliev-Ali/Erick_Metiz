massage = "Tell me something, and I will repeat it back to you: "
massage += "\nEnter 'quit' to end the program. "

active = True
while active:
    prompt = input(massage)

    if prompt == 'quit':
        active = False
    else:
        print(prompt)
        