text = "salom salom dunyo"

words = text.split()

result = {}

for word in words:
    result[word] = result.get(word, 0) + 1

print(result)
