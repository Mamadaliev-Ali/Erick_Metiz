def sandwich(name, **kwargs):
    kwargs['sandwich'] = name
    return kwargs


eat = sandwich('Сэндвич Монте-Кристо',
               restoran='Meat',
               location='Melbourne')
print(eat)
