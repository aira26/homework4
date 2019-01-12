with open('rosalind_dna.txt') as input_data:
    dna = input_data.read()                  #i opened the file in order to read it ans then i created an empty list,
                                            # in order to append it with  the result of the counting

count = []
for nucleotide in ['A', 'C', 'G', 'T']:
	count.append(str(dna.count(nucleotide)))

print (' '.join(count))

