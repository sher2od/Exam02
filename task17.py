numbers = [
    {'value': -5}, 
    {'value': 10}, 
    {'value': -1}, 
    {'value': 7}
]

positive_num = list(filter(lambda x: x['value'] > 0, numbers))

print(positive_num)
