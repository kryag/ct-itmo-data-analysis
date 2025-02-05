import numpy as np


def feature_matrix(args):
    result = []
    for arg in args:
        row = [1]
        for m in [12, 24, 168, 672]:
            row.append(np.sin(2 * np.pi * arg / m))
            row.append(np.cos(2 * np.pi * arg / m))
        result.append(row)
    return np.array(result)


if __name__ == '__main__':
    N = 168
    params, _, _, _ = np.linalg.lstsq(
        a=feature_matrix(np.arange(1, N + 1)),
        b=np.array([int(input()) for _ in range(N)])
    )
    print(*feature_matrix(np.arange(N + 1, 2 * N + 1)) @ params, sep='\n')
