import sys
input = lambda :sys.stdin.readline()

num=int(input())
data=list(map(int, input().split()))
num2=int(input())
data2=list(map(int,input().split()))

for i in range(len(data2)):
    if(data2[i] in data):
        data2[i]=1
    else:
        data2[i]=0
    print(data2[i], end=' ')
