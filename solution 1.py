numbers = [2, 1, 4, 3, 5]
result = []

for col in range(max(numbers)):
    result.append([])
    for row in range(len(numbers)):
        result[col].append(" ")

for i in range(len(numbers)):
    n = numbers[i]
    for j in range(n):
        result[-(j+1)][i] = "*"

for el in result:
    print(" ".join(el))