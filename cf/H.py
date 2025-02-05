from collections import defaultdict
import math

kx, ky = map(int, input().split())
N = int(input())

freq_pairs = defaultdict(int)
freq_x = defaultdict(int)

for _ in range(N):
    x, y = map(int, input().split())
    freq_pairs[(x, y)] += 1
    freq_x[x] += 1

result = 0
for (x, _), freq_xy in freq_pairs.items():
    result -= freq_xy / N * math.log(freq_xy / freq_x[x])

print(result)
