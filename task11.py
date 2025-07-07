import json

with open('Input/students.json') as json_file,open('Output/output11.json','w') as outo_file:
    data = json.load(json_file)
    print(data)


