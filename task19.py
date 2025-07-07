
names = ['Ali', 'Diyor', 'Jasurbek', 'Muhammad']


names = list(map(lambda student: student, names))


max_len = max(map(lambda name: len(name), names))


long_names = list(filter(lambda name: len(name) == max_len, names))

print("Eng  kop harfli ism  >> ")
print(long_names)
