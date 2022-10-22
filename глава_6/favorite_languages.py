favorite_languages = {
    'sara': ['C++', 'python'],
    'jen': ['PHP'],
    'edward': ['ruby', 'javaScript'],
    'phil': ['python', 'go'],
}

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}`s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")
