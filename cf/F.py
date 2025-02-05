def divide(a, b):
    if b == 0:
        return 0
    return a / b


if __name__ == '__main__':
    K = int(input())
    CM = [list(map(int, input().split())) for _ in range(K)]

    TP = [CM[i][i] for i in range(K)]
    FN = [sum(CM[i]) - CM[i][i] for i in range(K)]
    FP = [sum(CM[j][i] for j in range(K)) - CM[i][i] for i in range(K)]

    sum_CMs = [sum(row) for row in CM]
    sum_CM = sum(sum_CMs)

    calc_avg = lambda arr: sum(arr[i] * sum(CM[i]) for i in range(K)) / sum_CM
    TP_avg = calc_avg(TP)
    FP_avg = calc_avg(FP)
    FN_avg = calc_avg(FN)

    precisions = [divide(TP[i], TP[i] + FP[i]) for i in range(K)]
    recalls = [divide(TP[i], TP[i] + FN[i]) for i in range(K)]

    micro_precision = divide(TP_avg, TP_avg + FP_avg)
    micro_recall = divide(TP_avg, TP_avg + FN_avg)
    F_score_micro_avg = divide(2 * micro_precision * micro_recall, micro_precision + micro_recall)

    macro_precision = sum(precisions[i] * sum_CMs[i] for i in range(K)) / sum_CM
    macro_recall = sum(recalls[i] * sum_CMs[i] for i in range(K)) / sum_CM
    F_score_macro_avg = divide(2 * macro_precision * macro_recall, macro_precision + macro_recall)

    F_score_avg = sum(divide(2 * precisions[i] * recalls[i], precisions[i] + recalls[i]) * sum_CMs[i] for i in range(K)) / sum_CM

    print(F_score_micro_avg, F_score_macro_avg, F_score_avg, sep='\n')
