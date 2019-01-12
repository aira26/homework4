with open("rosalind_cons.txt","r") as f:
    np={}
    line=f.readline().strip()
    while line!='':
        name="".join(list(line)[1:len(line)])
        line=f.readline().strip()
        while line!='' and line[0]!=">":
            if name not in np:
                np[name]=line
            else:
                np[name]+=line
            line=f.readline().strip()

length=len(list(np.values())[0])
pros=[[0]*(length+1) for i in range(4)]

pros[0][0]="A:"
pros[1][0]="C:"
pros[2][0]="G:"
pros[3][0]="T:"

for name in np:
    for i in range(len(np[name])):
        if np[name][i]=="A":
            pros[0][i+1]+=1
        else:
            if np[name][i]=="C":
                pros[1][i+1]+=1
            else:
                if np[name][i]=="G":
                    pros[2][i+1]+=1
                else:
                    pros[3][i+1]+=1

cons=''
for i in range(length):
    a=[pros[j][i+1] for j in range(4)]
    m=max(a)
    maxs=[j for j, k in enumerate(a) if k==m]
    if maxs[0]==0:
        cons+="A"
    else:
        if maxs[0]==1:
            cons+="C"
        else:
            if maxs[0]==2:
                cons+="G"
            else:
                cons+="T"

print(cons)

for i in range(4):
    print(' '.join(map(str, pros[i])))