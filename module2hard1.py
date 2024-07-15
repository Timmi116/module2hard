import random

n = random.randint(3, 20)
pairs = []
for i in range(1, n):
    for j in range(i + 1, n + 1):
        if (i + j) % n == 0:
            pairs.append((i, j))
result = ''
for pair in pairs:
    result += ' '.join(map(str, pair)) + ' '
print(result)
