from collections import defaultdict


def calc_dist(x_list):
    n = len(x_list)
    pref = [0 for _ in range(n + 1)]

    for i in range(1, n + 1):
        pref[i] = pref[i - 1] + x_list[i - 1]

    return sum((x_list[i] * i - pref[i]) + ((pref[n] - pref[i + 1]) - x_list[i] * (n - i - 1)) for i in range(n))


if __name__ == '__main__':
    K, N = int(input()), int(input())

    classes = defaultdict(list)
    all_x = []

    for _ in range(N):
        x, y = map(int, input().split())
        classes[y].append(x)
        all_x.append(x)
    all_x.sort()

    classes_dist = sum(calc_dist(sorted(classes[y])) for y in classes)

    print(classes_dist)
    print(calc_dist(all_x) - classes_dist)
