from itertools import product

n,m=map(int, input().split())
data=list(range(1, n+1))

for i in product(data, repeat=m):
    for j in range(m):
        print(i[j], end=' ')
    print(sep='\n')
