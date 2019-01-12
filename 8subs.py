s,b= open('rosalind_subs.txt').read().split()
for i in range(len(s)):
    if s[i:].startswith(b):
        print(i+1)


