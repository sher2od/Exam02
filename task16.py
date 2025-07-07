
import csv

with open('Input/grades.csv', 'r') as csv_file, open('Output/output16.txt', 'w') as out_file:
    reader = csv.reader(csv_file)
    next(reader)  # Sarlavhasiz

    fives = list(filter(lambda row: row[1] == '5', reader))
    count = len(fives)

    out_file.write(f"5 baho olganlar soni: {count}")
