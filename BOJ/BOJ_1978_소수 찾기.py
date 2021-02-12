num=int(input())
data=list(map(int,input().split()))
ans=0
for i in range(num):
    cnt=0
    if data[i] != 1:
        for j in range(1,data[i]+1):
            if data[i]%j==0:
                cnt+=1
        if cnt==2:
            ans+=1
            print(data[i])
print(ans)
            
