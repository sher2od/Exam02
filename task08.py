with open('Input/numbers.txt') as f, open('Output/output08.txt', 'w') as ff:
    data = sum(int(x.strip()) for x in f)  
    print(data)
    ff.write(str(data)) 
