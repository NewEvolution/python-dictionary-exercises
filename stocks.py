stockDict = { 'GM': 'General Motors', 'CAT':'Caterpillar', 'EK':"Eastman Kodak" }

purchases = [
        ('GM', 100, '10-sep-2001', 48),
        ('CAT', 100, '1-apr-1999', 24),
        ('GM', 200, '1-jul-1998', 56) ,
        ('EK', 250, '9-jul-1999', 34)
        ]

summary = {}

print(''.join(['\033[4m\033[1m', 'Purchase History:', '\033[0m']))
for purch in purchases:
    if summary.setdefault(purch[0], [purch]) != [purch]:
        summary[purch[0]].append(purch)
    print(' '.join([
        '\t$' + str(purch[1] * purch[3]),
        'Purchase of', stockDict[purch[0]], 'on', purch[2],
        '(' + str(purch[1]), 'shares at', '$' + str(purch[3])  + ')'
        ]))

print(''.join(['\033[4m\033[1m', 'Purchase Summary:', '\033[0m']))
for corp, block in summary.items():
    print(''.join(['\033[1m', stockDict[corp], '\033[0m']))
    for data in block:
        print(' '.join([ '\t' + str(data[1]), 'shares at', '$' + str(data[3]), 'on', data[2] ]))

