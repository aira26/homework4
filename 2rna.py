with open('rosalind_rna.txt') as m:
	dna = m.read().strip()
print(dna.replace("T", "U"))
