import sys
input = lambda : sys.stdin.readline()

num=int(input())
for _ in range(num):
    people=int(input())
    data=[]
    result=1
    for _ in range(people):
        data.append(list(map(int, input().split())))
    data.sort()
    min=data[0][1]

    for i in range(1,people):
        if data[i][1]<min:
            min=data[i][1]
            result+=1
    print(result)