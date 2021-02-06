testNum=int(input())
result=[]
for i in range(testNum):
    ans=1
    n=0
    num, a=map(int, input().split())
    data=list(map(int, input().split()))
    for j in range(9,0,-1):
        if j in data:
            cnt=data.count(j)
            if data[a]==j:
                if cnt != 1:
                    idx=data.index(n)
                    if a>idx:
                        data[idx:a+1]
                        cnt=data.count(j)
                        ans+=cnt
                        break
                    else:
                        data1=data[idx:]
                        data2=data[:a+1]
                        cnt=data1.count(j)+data2.count(j)
                        ans=ans+cnt-1
                        break
                break
            else:
                ans+=cnt
                n=j
    result.append(ans)
for i in range(len(result)):
    print(result[i])
