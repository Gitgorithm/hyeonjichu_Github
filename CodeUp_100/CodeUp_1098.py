h,w=map(int, input().split())
list=[[0]*w for i in range(h)]
n=int(input())
for i in range(n):
    l,d,x,y=map(int, input().split())
    list[x-1][y-1]=1
    for j in range(l-1):
        if d==0:
            list[x-1][y]=1
            y+=1
        else:
            list[x][y-1]=1
            x+=1
for i in range(h):
    for j in range(w):
        print(list[i][j], end=' ')
    print()
