def send_massage(send_list, sent_message):
    while send_list:
        take_message = send_list.pop()
        print(f"Message: {take_message}")
        sent_message.append(take_message)


def show_massage(sent_message):
    print("\nShow motorcycles:")
    for show_list in sent_message:
        print("\t" + show_list)


send_lists = ["string", "number", "lists", "Dictionaries", "Tuples", "boolean", "sets"]
send_massages = []


send_massage(send_lists, send_massages)
show_massage(send_massages)
