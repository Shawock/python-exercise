from collections import OrderedDict

order_dict = OrderedDict()
order_dict['Zhouhao'] = 'Python'
order_dict['Jenny'] = 'Java'
order_dict['Sherman'] = 'Ruby'

for name, program_language in order_dict.items():
    print(name + " - " + program_language)

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
    print(name.title() + "'s favorite languages are: ")

    for language in languages:
        print("\t" + language)
