from itertools import combinations_with_replacement

n,m=map(int, input().split())
data=list(map(int, input().split()))
data.sort()

for i in combinations_with_replacement(data, m):
    for j in i:
        print(j, end=' ')
    print(sep='\n')
