K = int(input())
N = int(input())

categories = [[] for _ in range(K)]
dispersions = [0.0 for _ in range(K)]

for _ in range(N):
    x, y = map(int, input().split())
    categories[x - 1].append(y)

for i in range(K):
    if len(categories[i]) == 0:
        continue
    sum_ys = 0
    for y in categories[i]:
        sum_ys += y
    avg = sum_ys / len(categories[i])

    sum_diffs = 0
    for y in categories[i]:
        sum_diffs += pow(y - avg, 2)
    dispersions[i] = sum_diffs / len(categories[i])

sum_dispersions = 0
for i in range(K):
    sum_dispersions += len(categories[i]) * dispersions[i]

result = sum_dispersions / N
print(result)
