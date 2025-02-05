from collections import defaultdict
import math

N = int(input())
strs = [input() for _ in range(N)]
unigram_cnts, bigram_cnts = defaultdict(int), defaultdict(lambda: defaultdict(int))
for s in strs:
    for idx, char in enumerate(s):
        unigram_cnts[char] += 1
        if idx > 0:
            bigram_cnts[s[idx - 1]][char] += 1
result, max_prob = 0, 0
for idx, s in enumerate(strs, start=1):
    prob = sum(-math.log(
        (bigram_cnts[s[i - 1]].get(s[i], 0) + 1) / (sum(bigram_cnts[s[i - 1]].values()) + len(unigram_cnts))) for
               i in range(1, len(s)))
    if prob > max_prob:
        max_prob = prob
        result = idx
print(result)
