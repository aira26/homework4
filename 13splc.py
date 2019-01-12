import sys
file = open("Rosalind_splc.txt", "r")
count = 0
o = ""
s = ""
toS = ""

for x in file:
    o = x
    for y in x:
        if (count < 2):
            if (y == ">"):
                count = count +1
                break
            else:
                if (y == ">"):
                    count = count+1
                    break
                s = s.strip() + o.strip()
                break
        elif (count > 1):
            if ( y == ">"):
                break
            else:
                Snip = o
                s = s.replace(toS.strip(), '')

                break

DNA = s
index = 0
char = "U"
for x in DNA:
    if x == "T":
        DNA = DNA[:index] + char + s[index +1:]
    index = index +1
RNA = DNA



def decode(RNA):
  n=3
  x = [RNA [i:i+n] for i in range(0, len(RNA), n)] #splits them up into triplets
  for codon in x:
    if (protein(codon) == '.'):
      break
    sys.stdout.write(protein(codon))


def protein(codon):

    if (codon == 'UUU' or codon == 'UUC'):
        return ('F')
    elif (codon == 'UUA' or codon == 'UUG' or codon == 'CUU' or codon == 'CUC' or codon == 'CUA' or codon == 'CUG'):
        return ('L')
    elif (codon == 'UUA' or codon == 'UUG'):
        return ('L')
    elif (codon == 'AUU' or codon == 'AUC' or codon == 'AUA'):
        return ('I')
    elif (codon == 'AUG'):
        return ('M')
    elif (codon == 'GUU' or codon == 'GUC' or codon == 'GUA' or codon == 'GUG'):
        return ('V')
    elif (codon == 'UCU' or codon == 'UCC' or codon == 'UCA' or codon == 'UCG') or codon == 'AGU' or codon == 'AGC':
        return ('S')
    elif (codon == 'CCU' or codon == 'CCC' or codon == 'CCA' or codon == 'CCG'):
        return ('P')
    elif (codon == 'ACU' or codon == 'ACC' or codon == 'ACA' or codon == 'ACG'):
        return ('T')
    elif (codon == 'GCU' or codon == 'GCC' or codon == 'GCA' or codon == 'GCG'):
        return ('A')
    elif (codon == 'UAU' or codon == 'UAC'):
        return ('Y')
    elif (codon == 'UAA' or codon == 'UAG' or codon =='UGA'):
        return ('.')
    elif(codon == 'CAU' or codon == 'CAC'):
        return ('H')
    elif (codon == 'CAA' or codon == 'CAG'):
        return ('Q')
    elif (codon == 'AAU' or codon == 'AAC'):
        return ('N')
    elif (codon == 'AAA' or codon == 'AAG'):
       return ('K')
    elif(codon == 'GAU' or codon == 'GAC'):
        return ('D')
    elif (codon == 'GAA' or codon == 'GAG'):
        return ('E')
    elif (codon == 'UGU' or codon == 'UGC'):
        return ('C')
    elif (codon == 'UGG'):
        return ('W')
    elif (codon == 'CGU' or codon == 'CGC' or codon == 'CGA' or codon == 'CGG' or codon == 'AGA' or codon == 'AGG'):
        return ('R')
    elif (codon == 'GGU' or codon == 'GGC' or codon == 'GGA' or codon == 'GGG'):
        return ('G')

decode (RNA)


def rna_splicing(sequences):
    def dna_to_rna(sequence):
        return sequence.replace('T', 'U')
