from collections import deque

n, m, k = map(int, input().split(' '))

a = [list(map(int, input().split(' '))) for _ in range(n)]
graph = [[5] * n for _ in range(n)]
trees = [[deque() for _ in range(n)] for _ in range(n)]
dead_trees = [[list() for _ in range(n)] for _ in range(n)]
for _ in range(m):
    x, y, z = map(int, input().split(' '))
    trees[x - 1][y - 1].append(z)

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]


def spring_summer():
    for i in range(n):
        for j in range(n):
            len_ = len(trees[i][j])
            for k in range(len_):
                if graph[i][j] < trees[i][j][k]:
                    for _ in range(k, len_):
                        dead_trees[i][j].append(trees[i][j].pop())
                    break
                else:
                    graph[i][j] -= trees[i][j][k]
                    trees[i][j][k] += 1

    for i in range(n):
        for j in range(n):
            while dead_trees[i][j]:
                graph[i][j] += dead_trees[i][j].pop() // 2


def fall_winter():
    for i in range(n):
        for j in range(n):
            for k in range(len(trees[i][j])):
                if trees[i][j][k] % 5 == 0:
                    for l in range(8):
                        nx, ny, = i + dx[l], j + dy[l]

                        if nx < 0 or nx >= n or ny < 0 or ny >= n:
                            continue
                        trees[nx][ny].appendleft(1)

            graph[i][j] += a[i][j]


for i in range(k):
    spring_summer()
    fall_winter()

answer = 0
for i in range(n):
    for j in range(n):
        answer += len(trees[i][j])

print(answer)


# from collections import deque
#
# n, m, k = map(int, input().split())
# arr = [list(map(int, input().split())) for x in range(n)]   #S2D2
# a = [[5]*n for x in range(n)]
# direction = [[-1, 0], [1, 0], [0, 1], [0, -1], [-1, -1], [-1, 1], [1, -1], [1, 1]]
# tree = [[deque() for x in range(n)] for y in range(n)]
# tree5 = []
# for i in range(m):
#     x, y, age = map(int, input().split())
#     tree[x-1][y-1].append(age)
#
# def spring_summer():
#     for i in range(n):
#         for j in range(n):
#             for k in range(len(tree[i][j])):
#                 if a[i][j] < tree[i][j][k]:
#                     for l in range(len(tree[i][j])-k):
#                         a[i][j] += tree[i][j][k] // 2
#                         tree[i][j].pop()
#                     break
#                 else:
#                     a[i][j] -= tree[i][j][k]
#                     tree[i][j][k] += 1
#                     if tree[i][j][k] % 5 == 0:
#                         tree5.append([i, j, k])
#
# def fall():
#     global tree5
#     for i in range(len(tree5)):
#         for k in range(len(direction)):
#             nx = tree5[i][0] + direction[k][0]
#             ny = tree5[i][1] + direction[k][1]
#             if 0 <= nx < n and 0 <= ny < n:
#                 tree[nx][ny].appendleft(1)
#     tree5 = []
#
#
# def winter():
#     for i in range(n):
#         for j in range(n):
#             a[i][j] += arr[i][j]
#
# for i in range(k):
#     spring_summer()
#     fall()
#     winter()
#
# ans = 0
# for i in range(n):
#     for j in range(n):
#         ans += len(tree[i][j])
# print(ans)
