from itertools import product

n,m=map(int, input().split())
data=list(map(int, input().split()))
data.sort()

for i in product(data,repeat=m):
    for j in i:
        print(j, end=' ')
    print(sep='\n')
