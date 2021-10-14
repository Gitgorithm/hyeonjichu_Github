import itertools

n = int(input())
arr = [list(map(int, input().split())) for x in range(n)]
num = [x for x in range(1, n+1)]

p = list(map(list, itertools.combinations(num, int(n/2))))
p = p[:int(len(p)/2)]

answer = 99999

for i in range(len(p)):
    t1 = p[i]
    t2 = list(set(num) - set(p[i]))
    tmp1 = 0
    tmp2 = 0
    if len(t1) == 2:
        tmp1 = arr[t1[0]-1][t1[1]-1] + arr[t1[1]-1][t1[0]-1]
        tmp2 = arr[t2[0]-1][t2[1]-1] + arr[t2[1]-1][t2[0]-1]
    else:
        t1 = list(map(list, itertools.combinations(t1, 2)))
        t2 = list(map(list, itertools.combinations(t2, 2)))
        for k in range(len(t1)):
            tmp1 += arr[t1[k][0]-1][t1[k][1]-1] + arr[t1[k][1]-1][t1[k][0]-1]
            tmp2 += arr[t2[k][0]-1][t2[k][1]-1] + arr[t2[k][1]-1][t2[k][0]-1]
    answer = min(answer, max(tmp1, tmp2)-min(tmp1, tmp2))
print(answer)