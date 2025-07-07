import json
from pprint import pprint

with open('Input/students.json') as json_file, open('Output/output14.json', 'w') as outo_file:
    data = json.load(json_file)

    # A 
    a_names = list(filter(lambda student: student['name'].startswith('A'), data))

    
    pprint(a_names)

    # Faylga yozish
    json.dump(a_names, outo_file, indent=4)
