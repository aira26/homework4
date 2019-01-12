file = open('rosalind_prot.txt','r')
x = file.readlines()
data = ''.join(x)

codon_dict = {'UUU': 'F','CUU': 'L','AUU': 'I','GUU': 'V',
              'UUC': 'F','CUC': 'L','AUC': 'I','GUC': 'V',
              'UUA': 'L','CUA': 'L','AUA': 'I','GUA': 'V',
              'UUG': 'L','CUG': 'L','AUG': 'M','GUG': 'V',
              'UCU': 'S','CCU': 'P','ACU': 'T','GCU': 'A',
              'UCC': 'S','CCC': 'P','ACC': 'T','GCC': 'A',
              'UCA': 'S','CCA': 'P','ACA': 'T','GCA': 'A',
              'UCG': 'S','CCG': 'P','ACG': 'T','GCG': 'A',
              'UAU': 'Y','CAU': 'H','AAU': 'N','GAU': 'D',
              'UAC': 'Y','CAC': 'H','AAC': 'N','GAC': 'D',
              'UAA': 'Stop','CAA': 'Q','AAA': 'K','GAA': 'E',
              'UAG': 'Stop','CAG': 'Q','AAG': 'K','GAG': 'E',
              'UGU': 'C','CGU': 'R','AGU': 'S','GGU': 'G',
              'UGC': 'C','CGC': 'R','AGC': 'S','GGC': 'G',
              'UGA': 'Stop','CGA': 'R','AGA': 'R','GGA': 'G',
              'UGG': 'W','CGG': 'R','AGG': 'R','GGG': 'G'}



uplimit =len(data)+1
clist = []
index = []
codon = []
for i in range(0, len(data)):
    index.append(i)
for i in index:
    count = 0
    add = data[i]
    codon.append(add)
    if len(codon)==3:
        joindcodon = ''.join(codon)
        clist.append(joindcodon)
        del codon[:]

trn =[]
for i in clist:
    aa= codon_dict[i]
    if aa !='Stop':
        trn.append(aa)
print(''.join(trn))