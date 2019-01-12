file = open('rosalind_revp.txt').read().strip().split()

for i in range(len(file)):
    if file[i][0] == ">":
        file[i] = "-"

del file[0]
m = ''.join(file)
file = m.split('-')

a = file[0]

def revp(s):
    a = {'C':'G', 'G':'C', 'T':'A', 'A':'T'}
    transl = ""
    for letter in s:
        transl += a[letter]
    if transl == s[::-1]:
        return True
    else:
        return False

for i in range(0, len(a)):
    for j in range (4, 13):
        if revp(a[i:i+j]) and len(a[i:i+j])==j:
            print(str(i+1)+" "+str(j))