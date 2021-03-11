from itertools import permutations

n,m=map(int, input().split())
data=list(map(int, input().split()))
data.sort()

for i in permutations(data, m):
    for j in range(m):
        print(i[j], end=' ')
    print(sep='\n')
