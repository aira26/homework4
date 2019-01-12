import time

pd = open("rosalind_pdst.txt", "r")
dst = []
k = -1
for lin in pd:
    if lin.startswith(">"):
        k += 1
        dst.append("")
    else:
        dst[k] += lin.strip()
pd.close()


def prop(s1, s2):
    count = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            count += 1
    return 1.0000 * count / len(s1)


op = open("pdst.txt", "w")
tim = time.time()
for i in dst:
    for j in dst:
        d = prop(i, j)
        print(d)
        op.write(str(d) + " ")
    print
    ("")
    op.write("\n")

f = open("time.txt", "w")
f.write("Execution Time: " + str(time.time() - tim))
f.close()
