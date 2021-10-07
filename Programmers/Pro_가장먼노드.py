from collections import deque


def solution(n, edge):
    answer = 0
    route = [0] * (n + 1)
    edge.sort()
    queue = deque()
    graph = [[] for i in range(n + 1)]
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])

    queue.append(1)
    route[1] = 1
    while queue:
        now = queue.popleft()
        for g in graph[now]:
            if route[g] == 0:
                queue.append(g)
                route[g] = route[now] + 1
    for r in route:
        if r == max(route):
            answer += 1

    return answer