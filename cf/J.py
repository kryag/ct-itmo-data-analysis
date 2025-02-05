N = int(input())
objects = [tuple(map(int, input().split())) for _ in range(N)]
x1_sorted = {x: idx + 1 for idx, x in enumerate(sorted([obj[0] for obj in objects]))}
x2_sorted = {x: idx + 1 for idx, x in enumerate(sorted([obj[1] for obj in objects]))}
print(1 - (6 * sum((x1_sorted[x1] - x2_sorted[x2]) ** 2 for x1, x2 in objects)) / (N * (N ** 2 - 1)))
