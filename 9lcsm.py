def find(seq, t):
    lcsm = None
    for n in range(len(t)):
        if seq in t[n]:
            lcsm = 1
        else:
            lcsm = 0
    return lcsm

with open('rosalind_lcsm.txt', 'r') as f:
    s = []
    for line in f:
        if line[0] == '>':
            s.append('')
        else:
            s[-1] += line.rstrip()
s = sorted(s, key=len)

c = 0
d = 2
i = s[0]
eh = ''
p = 1
while c + len(eh) < len(i):
    meh = i[c:c + d]
    p = find(meh, s)
    if p == 1:
        d += 1
        eh = meh
    else:
        c += 1
print(eh)