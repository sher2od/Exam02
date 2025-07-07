import json

with open('Input/students.json') as json_file, open('Output/output12.json', 'w') as out_file:
    data = json.load(json_file)

    
    sorted_names = list(map(lambda student: student['name'], 
                sorted(data, key=lambda student: student['name'])))



    #faylga yozish
    json.dump({"sorted_names": sorted_names}, out_file, indent=4)
