numbers = [
    {'value': 2}, 
    {'value': 3}, 
    {'value': 4}
]

kv_numbers = list(map(lambda d: {'value': d['value'] ** 2}, numbers))

print(kv_numbers)
