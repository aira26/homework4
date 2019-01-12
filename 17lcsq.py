import sys

sys.setrecursionlimit(1500)
dna1 = ""
dna2 = ""

with open('rosalind_lcsq.txt', 'r') as f:
    f.readline()
    for line in f:
        if '>' in line:
            break
        else:
            dna1 += line.strip()

    for line in f:
        dna2 += line.strip()


def lcsq(s, t):
    m = len(s)
    n = len(t)
    C = [[0 for i in range(n + 1)] for j in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                C[i][j] = C[i - 1][j - 1] + 1
            else:
                C[i][j] = max(C[i][j - 1], C[i - 1][j])
    return C


def lcsq_len(C):

    return C[-1][-1]


def backtrack(C, s, t, i, j):

    if i == 0 or j == 0:
        return ""
    elif s[i - 1] == t[j - 1]:
        return backtrack(C, s, t, i - 1, j - 1) + s[i - 1]
    else:
        if C[i][j - 1] > C[i - 1][j]:
            return backtrack(C, s, t, i, j - 1)
        else:
            return backtrack(C, s, t, i - 1, j)


C = lcsq(dna1, dna2)
print(lcsq_len(C))
print(backtrack(C, dna1, dna2, len(dna1), len(dna2)))