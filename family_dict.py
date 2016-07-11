my_family = {'brother': {'name': 'Travis', 'age': 32}, 'sister': {'name': 'Brooke', 'age': 34}}

#[print(' '.join([v['name'], 'is my', k, 'and is', str(v['age']), 'years old'])) for k, v in my_family.items()]
[print('{0} is my {1} and is {2} years old'.format(v['name'], k, v['age'])) for k, v in my_family.items()]
