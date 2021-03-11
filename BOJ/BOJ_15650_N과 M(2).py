from itertools import combinations

n,m=map(int, input().split())
data=list(range(1, n+1))

for i in combinations(data,m):
    for j in range(m):
        print(i[j], end=' ')
    print(sep='\n')
