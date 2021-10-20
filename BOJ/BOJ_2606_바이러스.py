num = int(input())
n = int(input())
arr = [[] for x in range(num+1)]
visited = [False] * (num+1)

for i in range(n):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

def dfs(node):
    visited[node] = True
    for i in arr[node]:
        if not visited[i]:
            dfs(i)

dfs(1)
print(visited.count(True)-1)