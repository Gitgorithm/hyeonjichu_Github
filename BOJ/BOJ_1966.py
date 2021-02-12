testNum=int(input())    #test 개수
result=[]   #결과 저장
for i in range(testNum):
    ans=1
    n=0
    num, a=map(int, input().split())
    data=list(map(int, input().split()))
    for j in range(9,0,-1): 
        if j in data:   #9부터 1까지 반복하면서 해당 숫자가 있는경우
            cnt=data.count(j)   #몇 개 반복되는지 찾기
            if data[a]==j:  #찾는 숫자와 같은경우
                if cnt != 1:    
                    idx=data.index(n)
                    if a>idx:   #가장 최근 index(idx)보다 찾는 수의 index(a)가 크면 수를 세서 더함
                        data[idx:a+1]
                        cnt=data.count(j)
                        ans+=cnt
                        break
                    else:   #아니면 idx의 뒤의 개수와 앞의 개수를 같이 더해줌
                        data1=data[idx:]
                        data2=data[:a+1]
                        cnt=data1.count(j)+data2.count(j)
                        ans=ans+cnt-1
                        break
                break
            else:   #찾는 숫자와 다른경우 => 중요도를 의미하는 ans에 cnt수만큼 더하기
                ans+=cnt
                n=j
    result.append(ans)
for i in range(len(result)):
    print(result[i])
