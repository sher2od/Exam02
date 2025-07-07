with open('Input/numbers.txt') as f, open('Output/output09.txt', 'w') as ff:
    data = max(f, key=lambda x: int(x.strip()))
    ff.write(data)
