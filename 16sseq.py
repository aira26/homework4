f = open('rosalind_sseq.txt', 'r')
matt = []
i = 0
s=''
b=''
while f:
    b = f.readline().strip()
    if b == '':
        matt.append(s)
        break
    if b[0] is not '>':
        s = s + b
    else:
        if len(s):
            matt.append(s)
            s=''
j=0
for i in matt[1]:
    j = matt[0].find(i, j+1)
    print (j+1)