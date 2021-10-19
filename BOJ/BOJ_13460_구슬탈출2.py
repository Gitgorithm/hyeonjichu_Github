from collections import deque

n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
visited = [[[[False] * m for x in range(n)]for y in range(m)] for z in range(n)]
direction = [[-1, 0], [0, -1], [1, 0], [0, 1]]

for i in range(n):
    for j in range(m):
        if arr[i][j] == 'R':
            ri, rj = i, j
        elif arr[i][j] == 'B':
            bi, bj = i, j

queue = deque()
queue.append([ri, rj, bi, bj, 0])
visited[ri][rj][bi][bj] = True

def move(x, y, dx, dy, c):
    while arr[x+dx][y+dy] != '#' and arr[x][y] != 'O':
        x += dx
        y += dy
        c += 1
    return x, y, c

while queue:
    rx, ry, bx, by, cnt = queue.popleft()
    if cnt >= 10:
        break
    for k in range(4):
        nrx, nry, rc = move(rx, ry, direction[k][0], direction[k][1], 0)
        nbx, nby, bc = move(bx, by, direction[k][0], direction[k][1], 0)
        if arr[nbx][nby] == 'O':
            continue
        if arr[nrx][nry] == 'O':
            print(cnt + 1)
            exit()
        if nrx == nbx and nry == nby:
            if rc > bc:
                nrx -= direction[k][0]
                nry -= direction[k][1]
            else:
                nbx -= direction[k][0]
                nby -= direction[k][1]
        if not visited[nrx][nry][nbx][nby]:
            queue.append([nrx, nry, nbx, nby, cnt+1])
            visited[nrx][nry][nbx][nby] = True
print(-1)