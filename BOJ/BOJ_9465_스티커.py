import sys
input=lambda: sys.stdin.readline()

num=int(input())

for i in range(num):
    n=int(input())
    data=[[x for x in map(int, input().split())] for y in range(2)]
    score=[[0 for x in range(n)]for y in range(2)]
    score[0][0]=data[0][0]
    score[1][0]=data[1][0]
    score[0][1]=data[1][0]+data[0][1]
    score[1][1]=data[0][0]+data[1][1]

    for j in range(2,n):
        score[0][j]=max(score[1][j-1],score[1][j-2])+data[0][j]
        score[1][j]=max(score[0][j-1],score[0][j-2])+data[1][j]
    print(max(score[0][n-1],score[1][n-1]))
