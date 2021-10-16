import itertools
import copy
from collections import deque

n, m = map(int, input().split())
a = [list(map(int, input().split())) for x in range(n)]

zero = []   #0인 공간 인덱스 담아두기
virus = []  #바이러스 인덱스 담아두기
direction = [[-1, 0], [0, -1], [1, 0], [0, 1]]  #상하좌우 검사하기 위한 방향
ans = 0

#0, 2인 자리를 각각 검사한다.
for i in range(n):
    for j in range(m):
        if a[i][j] == 0:
            zero.append([i, j])
        elif a[i][j] == 2:
            virus.append([i, j])

#combinations을 이용해서 0을 3개 선택할 수 있는 모든 경우를 구한다.
com = list(itertools.combinations(zero, 3))
for i in range(len(com)):
    result = 0
    v = deque(virus)
    arr = copy.deepcopy(a)
    #선택된 3개의 영역을 벽으로 변경한다.
    arr[com[i][0][0]][com[i][0][1]] = 1
    arr[com[i][1][0]][com[i][1][1]] = 1
    arr[com[i][2][0]][com[i][2][1]] = 1
    while v:
        x, y = v.popleft()
        for k in range(4):
            nx = x + direction[k][0]
            ny = y + direction[k][1]
            #범위에 맞고 0인 곳은 바이러스가 퍼지므로 2로 변경한다.
            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 0:
                    v.append([nx, ny])
                    arr[nx][ny] = 2
    #0인 곳의 수를 세어 더한다.
    for j in range(n):
        result += arr[j].count(0)
    ans = max(ans, result)
print(ans)
