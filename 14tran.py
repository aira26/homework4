def problem(s1, s2):
    transitions = set([('A', 'G'), ('G', 'A'), ('C', 'T'), ('T', 'C')]) # set() method is used to convert any of the iterable
                                                                # to the distinct element and sorted sequence of iterable elements,
    r = {True: 0.0, False: 0.0}
    for p in zip(s1, s2):
        if p[0] != p[1]:
            r[p in transitions] += 1
    return r[True] / r[False]
def fast(file):
    data = open(file).readlines()
    records = {}
    recordid = 0
    for line in data:

        if line.startswith('>'):
            recordid = line[1:].rstrip()

            records[recordid] = ''
        else:


            records[recordid] += line.rstrip()
    return records



test = fast('rosalind_tran.txt')
key,s2 = test.popitem()
key,s1 = test.popitem()

print(problem(s1, s2))