import json
from pprint import pprint

with open('Input/students.json', 'r') as json_file:
    data = json.load(json_file)

# Ismlar ro'yxati
names = list(map(lambda student: student['name'], data))

# Eng qisqa ism uzunligi
min_len = min(map(lambda name: len(name), names))


shortest_names = list(filter(lambda name: len(name) == min_len, names))

print("Eng kam harfli ism  >> ")
pprint(shortest_names)
