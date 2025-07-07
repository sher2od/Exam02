students = {'Ali': 5, 'Vali': 4, 'Hasan': 5, 'Husan': 3}


avg = sum(students.values()) / len(students)

# O'rtachadan yuqori baholilarni filter + lambda bilan
high_scores = list(filter(lambda name: students[name] > avg, students))

print(f"O‘rtacha baho: {avg}")
print(f"{avg} dan yuqorilar: {', '.join(high_scores)}")
