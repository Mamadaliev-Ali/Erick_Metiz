def print_model(unprinted_designs, completed_models):
    """
     Имитирует печать моделей, пока список не станет пустым.
     Каждая млдель после печати перемещается в completed_models
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """Выводит информацию обо всех напечатаных моделях"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print("\t" + completed_model)


unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_model(unprinted_designs[:], completed_models)
show_completed_models(completed_models)