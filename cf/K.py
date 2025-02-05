def dist(a, b):
    return abs(a - b)


n = int(input())
data = [tuple(map(int, input().split())) for _ in range(n)]
data.sort(key=lambda e: e[0])
xs, pref_sum_ys = [d[0] for d in data], [d[1] for d in data]
for i in range(1, n):
    pref_sum_ys[i] += pref_sum_ys[i - 1]

for _ in range(int(input())):
    x_q, k_q = map(int, input().split())

    left, right = 0, n
    while left + 1 != right:
        mid = (left + right) // 2
        if xs[mid] <= x_q:
            left = mid
        else:
            right = mid
    idx = left if right == n or xs[left] == x_q or dist(x_q, xs[left]) <= dist(xs[right], x_q) else right

    left = right = idx
    k_q -= 1
    while k_q != 0:
        step = 1 if k_q == 1 else k_q // 2
        next_left, next_right = max(left - step, 0), min(right + step, n - 1)
        if right == next_right or (left != next_left and dist(x_q, xs[next_left]) <= dist(xs[next_right], x_q)):
            k_q -= left - next_left
            left = next_left
        else:
            k_q -= next_right - right
            right = next_right
    if left > 0 and (xs[left - 1] == xs[left] or dist(x_q, xs[left - 1]) == dist(xs[right], x_q)):
        print(-1.0)
        continue
    if right < n - 1 and (xs[right + 1] == xs[right] or dist(x_q, xs[right + 1]) == dist(x_q, xs[left])):
        print(-1.0)
        continue
    sum_ys = pref_sum_ys[right] - (pref_sum_ys[left - 1] if left > 0 else 0)
    print(sum_ys / (right - left + 1))
