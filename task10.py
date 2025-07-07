with open('Input/numbers.txt') as f, open('Output/output10.txt', 'w') as ff:
    data = sorted(f, key=lambda x: x)  
    for line in data:
        ff.write(line)
