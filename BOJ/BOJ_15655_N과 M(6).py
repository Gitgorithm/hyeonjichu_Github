from itertools import combinations

n,m=map(int, input().split())
data=list(input().split())

for i in combinations(data, m):
    for j in range(m):
        print(i[j], end=' ')
    print(sep='\n')
