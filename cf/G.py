N, K = map(int, input().split())
classes = list(map(int, input().split()))

pref_cnts = [0] * K
suff_cnts = [0] * K
for c in classes:
    suff_cnts[c - 1] += 1

subset1_sum_cnts = 0
subset2_sum_cnts = sum(count ** 2 for count in suff_cnts)

for i in range(1, N):
    cur_class = classes[i - 1] - 1

    subset1_sum_cnts += 2 * pref_cnts[cur_class] + 1
    pref_cnts[cur_class] += 1

    subset2_sum_cnts += -2 * suff_cnts[cur_class] + 1
    suff_cnts[cur_class] -= 1

    subset1_gini_index = 1 - subset1_sum_cnts / i ** 2
    subset2_gini_index = 1 - subset2_sum_cnts / (N - i) ** 2
    print((i * subset1_gini_index + (N - i) * subset2_gini_index) / N)
