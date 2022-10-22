users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'aeinstein',
        'location': 'princeton',
    },

    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

for user_name, user_info in users.items():
    print(f"\nUsername: {user_name}")
    fullName = f"{user_info['first']} {user_info['last']}"
    location = f"{user_info['location']}"
    print(f"\tFull Name: {fullName}")
    print(f"\tLocation: {location}")