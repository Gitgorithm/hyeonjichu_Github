import sys
from collections import deque

def dfs(graph,v,visited):
    visited[v]=True
    print(v,end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

def bfs(graph,start,visited):
    queue=deque([start])
    visited[start]=True

    while queue:
        v=queue.popleft()
        print(v,end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

n,m,v=map(int, sys.stdin.readline().split())
data=[[]]*(m+1)
graph=[[]]
for i in range(1,m+1):    #데이터 입력 받기
    data[i]=list(map(int,sys.stdin.readline().split()))

for i in range(1,n+1):
    s = set()
    for j in data:    #입력받은 데이터 하나씩 조사
        if i in j:    #i가 있으면
            for k in j:    #집합에 추가하기
                s.add(k)
            s.remove(i)    #해당 순서인 숫자 지우기
    sList=list(s)
    sList.sort()
    graph.insert(i,sList)    #그래프에 추가해서 그래프 생성

visited=[False]*(n+1)
dfs(graph,v,visited)
print()
visited=[False]*(n+1)
bfs(graph,v,visited)
