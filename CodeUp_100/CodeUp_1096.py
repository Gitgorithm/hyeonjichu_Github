list=[[0]*19 for i in range(19)]
num=int(input())

for i in range(1,num+1):
    a=input().split()
    list[int(a[0])-1][int(a[1])-1]=1
    
for i in range(19):
    for j in range(19):
        print(list[i][j], end=' ')
    print()
