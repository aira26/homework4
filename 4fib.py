def fibo(n,m):
    if n < 2:
        return n
    else:
        return fibo(n-1,m)+(fibo(n-2,m)*m)

with open('rosalind_fib.txt') as m:
	n,m = map(int, m.read().split())

no = str(fibo(n,m))
print(no)

with open('FIBO.txt', 'w') as n:
    n.write(no)