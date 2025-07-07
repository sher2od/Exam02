import csv

with open('Input/grades.csv') as csv_file, open('Output/output15.txt', 'w') as write_file:
    reader = csv.reader(csv_file)
    next(reader)  # Sarlavhasiz

    max_score = max(reader, key=lambda row: int(row[1]))
    #print(max_score)

    #write_file.write(f"Bahosi eng yuqori o‘quvchi:{max_score}")
    write_file.write(f"Bahosi eng yuqori o‘quvchi: {max_score[0]} - {max_score[1]}")
