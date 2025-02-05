N, K = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

k_to_indexes = {i: [] for i in range(1, K + 1)}
for i in range(N):
    k_to_indexes[a[i]].append(i)

b_sum = sum(b)
b_avg = b_sum / N
b_sum_sqrs = sum((b[i] - b_avg) ** 2 for i in range(N))

result = 0
for k in range(1, K + 1):
    indexes = k_to_indexes[k]
    cur_len = len(indexes)
    if cur_len == 0:
        continue
    a_avg = cur_len / N
    b_idx_sum = sum(b[i] for i in indexes)
    numerator = sum((1 - a_avg) * (b[i] - b_avg) for i in indexes) - (b_sum - b_idx_sum - b_avg * (N - cur_len)) * a_avg
    denominator = ((((1 - a_avg) ** 2) * cur_len + (a_avg ** 2) * (N - cur_len)) * b_sum_sqrs) ** 0.5
    result += cur_len * (numerator / denominator) if denominator != 0 else 0

result /= N
print(result)
