from itertools import combinations_with_replacement

n,m=map(int, input().split())
data=list(range(1,n+1))

for i in combinations_with_replacement(data,m):
    for j in range(m):
        print(i[j], end=' ')
    print(sep='\n')
