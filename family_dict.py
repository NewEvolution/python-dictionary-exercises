my_family = {'brother': {'name': 'Travis', 'age': 32}, 'sister': {'name': 'Brooke', 'age': 34}}

for k, v in my_family.items():
    print(' '.join([v['name'], 'is my', k, 'and is', str(v['age']), 'years old']))
