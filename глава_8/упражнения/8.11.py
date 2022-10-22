def great_user(last_name, first_name, **kwargs):
    kwargs['last'] = last_name
    kwargs['first'] = first_name
    return kwargs


user = great_user('James', 'Bond',
                  location='England',
                  age='45',
                  car='Aston Martin',
                  )
print(user)