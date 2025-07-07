import json

with open('Input/students.json') as json_file, open('Output/output13.json', 'w') as out_file:
    data = json.load(json_file)



    long_names = list(
    map(lambda student: student['name'], 
        filter(lambda student: len(student['name']) > 5, data))
)


    json.dump({"long_names": long_names}, out_file, indent=4)
