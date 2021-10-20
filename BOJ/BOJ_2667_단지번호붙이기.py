#BFS
from collections import deque

n = int(input())
arr = [list(map(int, input().strip())) for x in range(n)]

direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]
ans = []
def bfs():
    queue = deque()
    queue.append([i, j])
    arr[i][j] = 2
    cnt = 1
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + direction[k][0]
            ny = y + direction[k][1]
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 1:
                queue.append([nx, ny])
                arr[nx][ny] = 2
                cnt += 1
    ans.append(cnt)


for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            bfs()

ans.sort()
print(len(ans))
for i in range(len(ans)):
    print(ans[i])




#DFS
# n = int(input())
# arr = [list(map(int, input().strip())) for x in range(n)]
#
# direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]
# visited = [[False]*n for x in range(n)]
# ans = []
#
# def dfs(x, y):
#     global cnt
#     cnt += 1
#     visited[x][y] = True
#     for k in range(4):
#         nx = x + direction[k][0]
#         ny = y + direction[k][1]
#         if 0 <= nx < n and 0 <= ny <n and not visited[nx][ny] and arr[nx][ny] == 1:
#             dfs(nx, ny)
#
#
# for i in range(n):
#     for j in range(n):
#         if arr[i][j] == 1 and not visited[i][j]:
#             cnt = 0
#             dfs(i, j)
#             ans.append(cnt)
#
# ans.sort()
# print(len(ans))
# for i in range(len(ans)):
#     print(ans[i])

