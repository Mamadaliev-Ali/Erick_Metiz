
def describe_pet(animal_type, pet_name):
    """ Позиционные аргументы """
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()} ")


describe_pet("hamster", "harry")

"""именнованые аргументы"""
describe_pet(animal_type='dog', pet_name='willie')
