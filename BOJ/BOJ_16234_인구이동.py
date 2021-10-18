#pypy3로 제출해야 시간초과 막을 수 있음
from collections import deque

n, l, r = map(int, input().split())
arr = [list(map(int, input().split())) for x in range(n)]

direction = [[-1, 0], [0, -1], [1, 0], [0, 1]]  #반시계 방향
ans = 0


def bfs(start):
    global move
    queue = deque()
    queue.append(start)
    visited[start[0]][start[1]] = True
    s = arr[start[0]][start[1]]
    tmp = [start]
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + direction[k][0]
            ny = y + direction[k][1]
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and l <= abs(arr[nx][ny] - arr[x][y]) <= r:
                    queue.append([nx, ny])
                    visited[nx][ny] = True
                    tmp.append([nx, ny])
                    s += arr[nx][ny]
    if len(tmp) > 1:
        move = True
        for t in range(len(tmp)):
            arr[tmp[t][0]][tmp[t][1]] = int(s / len(tmp))


while True:
    visited = [[False]*n for x in range(n)]
    move = False
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                bfs([i, j])
    if move:
        ans += 1
    else:
        print(ans)
        break