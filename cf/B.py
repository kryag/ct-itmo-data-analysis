import math


if __name__ == '__main__':
    eps = 1e-14
    K = int(input())
    fines = list(map(int, input().split()))
    a = int(input())

    word_class_frequencies = [dict() for _ in range(K)]
    class_frequencies = [0] * K
    all_words = set()

    N = int(input())
    for _ in range(N):
        clazz, count_words, *words = input().split()
        clazz = int(clazz) - 1
        class_frequencies[clazz] += 1
        unique_words = set(words)
        for word in unique_words:
            word_class_frequencies[clazz][word] = word_class_frequencies[clazz].setdefault(word, 0) + 1
            all_words.add(word)

    for [all_messages, words_dict] in zip(class_frequencies, word_class_frequencies):
        denom = all_messages + 2 * a
        for word in all_words:
            if word in words_dict:
                words_dict.update({word: (words_dict[word] + a) / denom})
            else:
                words_dict[word] = a / denom

    M = int(input())
    for _ in range(M):
        count_words, *words = input().split()
        unique_words = set(words)
        class_probabilities = [math.log(fines[i]) + math.log(class_frequencies[i] / N + eps) for i in range(0, K)]
        for clazz in range(K):
            for [train_word, cond_prob] in word_class_frequencies[clazz].items():
                prob = cond_prob if train_word in unique_words else (1 - cond_prob)
                class_probabilities[clazz] += math.log(prob + eps)
        max_class_prob = max(class_probabilities)
        final_class_probabilities = [math.exp(class_prob - max_class_prob) for class_prob in class_probabilities]
        denom = sum(final_class_probabilities)
        for clazz in range(K):
            print(final_class_probabilities[clazz] / denom, end=' ')
        print()
