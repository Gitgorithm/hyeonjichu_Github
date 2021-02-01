a=[]
for i in range(19):
    a.append(list(map(int, input().split())))
num=int(input())
for i in range(num):
    x,y=map(int, input().split())
    #가로줄 변경
    for i in range(19):
        if a[x-1][i]==1:
            a[x-1][i]=0
        elif a[x-1][i]==0:
            a[x-1][i]=1
    #세로줄 변경
    for i in range(19):
        if a[i][y-1]==1:
            a[i][y-1]=0
        elif a[i][y-1]==0:
            a[i][y-1]=1
for i in range(19):
    for j in range(19):
        print(a[i][j], end=' ')
    print()
