import itertools

def perm(int):
	first = ''
	for i in range(1,int+1):
		first += str(i)
	perm = ([x for x in itertools.permutations(first)])
	print(len(perm))
	for i in perm:
		print(' '.join(map(str, i)))

#Test
perm(4)