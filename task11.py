import json

with open('Input/students.json') as json_file:
    data = json.load(json_file)

student_num = len(data)

with open('Output/output11.json', 'w') as outo_file:
    json.dump({"count": student_num}, outo_file,indent=2)
