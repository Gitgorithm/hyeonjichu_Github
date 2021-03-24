import sys
from collections import deque

def bfs(data):
    queue=deque()
    #상,하,좌,우,대각선 모두 검사
    a=[0, 0, 1, -1, 1, -1, 1, -1]
    b=[1, -1, 0, 0, 1, -1, -1, 1]
    cnt=0   #섬 개수
    for i in range(h):
        for j in range(w):
            if data[i][j]==1 and visited[i][j] == False:
                queue.append(i)
                queue.append(j)
                visited[i][j]=True
                while queue:
                    x=queue.popleft()
                    y=queue.popleft()
                    for k in range(0,8):    #자기 기준으로 주변에 1이 있나 검사
                        p=x+int(a[k])   #x+=int(a[k])   => 이렇게 하면 x,y값이 계속 갱신돼서 안됨
                        q=y+int(b[k])   #y+=int(b[k])
                        if 0<=int(p)<h and 0<=int(q)<w and data[p][q]==1 and visited[p][q]==False:
                            queue.append(p)
                            queue.append(q)
                            visited[p][q]=True
                cnt+=1
    print(cnt)

w, h=map(int, sys.stdin.readline().split())

while (w != 0 and h !=0):
    data=[[x for x in map(int, sys.stdin.readline().split())] for y in range(h)]
    visited=[[False for _ in range(w)] for _ in range(h)]

    bfs(data)

    w, h = map(int,sys.stdin.readline().split())