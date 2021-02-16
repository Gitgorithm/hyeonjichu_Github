import math

num=int(input())
data=list(map(int,input().split()))
num_list=list(range(2,1001))    #1은 소수가 아니므로 제외, 1000까지의 수
cnt=0

for i in range(2,math.ceil(math.sqrt(1000))):   #ceil = 올림
    for j in num_list:
        if j/i == 1:    #자신과 같으면 pass
            pass
        elif j%i==0:    #자신과 같지 않고 나눈 나머지가 0이면 소수가 아님
            num_list.remove(j)  #소수가 아닌 수는 제거
for k in data:
    if k in num_list:   #리스트에서 소수 찾기 
        cnt+=1
print(cnt)            
