import re

def fastaRead(filename):
    fasta = {}
    with open(filename, "r") as file_one:
        for line in file_one:
            line = line.strip()
            if not line:
                continue
            if line.startswith(">"):
                active_sequence_name = line[1:]
                if active_sequence_name not in fasta:
                    fasta[active_sequence_name] = []
                continue
            sequence = line
            fasta[active_sequence_name].append(sequence)
        numberDictKey = len(fasta)
        numberOfValueInKey = 0
        singleDna = ""
        for numberDictKey in fasta:
            valuesInKey = fasta[numberDictKey]
            numberOfValueInKey = len(valuesInKey)

            for numberOfValueInKey in valuesInKey:
                singleDna += numberOfValueInKey

                fasta[numberDictKey] = singleDna
            singleDna = ""
    return fasta


def reverse_comp(dnaStrand):

    # This gets the reverse complement of the strand
    complementDNA = ""

    dnaSequence = list(dnaStrand)
    dnaSequence.reverse()

    dnaStrand = ''.join(dnaSequence)
    complementDict = {"C": "G", "G": "C", "T": "A", "A": "T"}

    for base in dnaStrand:
        complementDNA += complementDict[base]

    return complementDNA

def reading_frames(dna):
    frames=[]
    frames += dna, dna[1:],dna[2:]
    rc = "temp"
    rc = reverse_comp(dna)
    frames += rc, rc[1:],rc[2:]
    return frames


def translateRnaToProteins (rna):
    lenOfStr = len(rna)
    newStr = ""
    a = 0
    b = 3
    i = 0

    str = rna[a:b]

    while i < lenOfStr:
        if "UUU" in str:
            newStr += 'F'
        if "UUC" in str:
            newStr += 'F'
        if "UUA" in str:
            newStr += 'L'
        if "UUG" in str:
            newStr += 'L'

        if "UCU" in str:
            newStr += 'S'
        if "UCC" in str:
            newStr += 'S'
        if "UCA" in str:
            newStr += 'S'
        if "UCG" in str:
            newStr += 'S'

        if "UAU" in str:
            newStr += 'Y'
        if "UAC" in str:
            newStr += 'Y'
        if "UAA" in str:
            newStr += '*'
        if "UAG" in str:
            newStr += '*'

        if "UGU" in str:
            newStr += 'C'
        if "UGC" in str:
            newStr += 'C'
        if "UGA" in str:
            newStr += '*'
        if "UGG" in str:
            newStr += 'W'

        if "CUU" in str:
            newStr += 'L'
        if "CUC" in str:
            newStr += 'L'
        if "CUA" in str:
            newStr += 'L'
        if "CUG" in str:
            newStr += 'L'

        if "CCU" in str:
            newStr += 'P'
        if "CCC" in str:
            newStr += 'P'
        if "CCA" in str:
            newStr += 'P'
        if "CCG" in str:
            newStr += 'P'

        if "CAU" in str:
            newStr += 'H'
        if "CAC" in str:
            newStr += 'H'
        if "CAA" in str:
            newStr += 'Q'
        if "CAG" in str:
            newStr += 'Q'

        if "CGU" in str:
            newStr += 'R'
        if "CGC" in str:
            newStr += 'R'
        if "CGA" in str:
            newStr += 'R'
        if "CGG" in str:
            newStr += 'R'

        if "AUU" in str:
            newStr += 'I'
        if "AUC" in str:
            newStr += 'I'
        if "AUA" in str:
            newStr += 'I'
        if "AUG" in str:
            newStr += 'M'

        if "ACU" in str:
            newStr += 'T'
        if "ACC" in str:
            newStr += 'T'
        if "ACA" in str:
            newStr += 'T'
        if "ACG" in str:
            newStr += 'T'

        if "AAU" in str:
            newStr += 'N'
        if "AAC" in str:
            newStr += 'N'
        if "AAA" in str:
            newStr += 'K'
        if "AAG" in str:
            newStr += 'K'

        if "AGU" in str:
            newStr += 'S'
        if "AGC" in str:
            newStr += 'S'
        if "AGA" in str:
            newStr += 'R'
        if "AGG" in str:
            newStr += 'R'

        if "GUU" in str:
            newStr += 'V'
        if "GUC" in str:
            newStr += 'V'
        if "GUA" in str:
            newStr += 'V'
        if "GUG" in str:
            newStr += 'V'

        if "GCU" in str:
            newStr += 'A'
        if "GCC" in str:
            newStr += 'A'
        if "GCA" in str:
            newStr += 'A'
        if "GCG" in str:
            newStr += 'A'

        if "GAU" in str:
            newStr += 'D'
        if "GAC" in str:
            newStr += 'D'
        if "GAA" in str:
            newStr += 'E'
        if "GAG" in str:
            newStr += 'E'

        if "GGU" in str:
            newStr += 'G'
        if "GGC" in str:
            newStr += 'G'
        if "GGA" in str:
            newStr += 'G'
        if "GGG" in str:
            newStr += 'G'

        a += 3
        b += 3
        str = rna[a:b]

        i += 1

    return newStr


dnaDict = fastaRead("rosalind_orf.txt")
readingFrames = []
#Actual code for this program
for i in dnaDict:
    dnaStrand = dnaDict[i]
#This gets the reverse complement of the strand and store it in a new list
    readingFrames += reading_frames(dnaStrand)

#Now we need to convert all of the DNA strands with T's with U's i.e. RNA
count = 0
for i in readingFrames:
    dnaWithT = i
    dnaWithU = ""
    dnaWithU = dnaWithT.replace("T","U")
    readingFrames[count] = dnaWithU
    count += 1

for i in readingFrames:
    print(i)

#Now we go and turn these RNA's into proteins
count = 0
for i in readingFrames:
    rna = i
    protein = translateRnaToProteins(rna)
    readingFrames[count] = protein
    count += 1
#Now we need to print every sequence that starts with an M in each strand

for i in readingFrames:
    print (i)

transcriptionList = []
for i in readingFrames:
    proteinStrand = i
    charM = 'M'
    startMPos = [pos for pos, char in enumerate(proteinStrand) if char == charM]
    if not startMPos:
        continue
    else:
        for j in startMPos:
            transcription = proteinStrand[j:]
            transcriptionList.append(transcription)

transcriptionList.reverse()
print(transcriptionList)

m_proteins = []

for i in readingFrames:
    stop_index = []
    starting_index = []
    for j in re.finditer('M', i):
        starting_index.append(j.start())
    for j in re.finditer('\*', i):
        stop_index.append(j.start())
    for j in starting_index:
        for k in stop_index:
            if k > j:
                if i[j:k] not in m_proteins:
                    m_proteins.append(i[j:k])
                break

for i in m_proteins:
    print(i)