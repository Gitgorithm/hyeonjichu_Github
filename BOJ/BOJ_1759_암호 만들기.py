from itertools import combinations

def check(chkList):     #모음 개수 세기
    cnt=0
    for i in chkList:
        if i in ['a','e','i','o','u']:
            cnt+=1
    return cnt
      
l,c = map(int, input().split())
data=list(input().split())
data.sort() #순서대로 정렬

if 3<=l<=c<=15 and len(data)==c:    #입력 조건
    for i in combinations(data, l):     #중복없는 l개 조합
        if check(i)>=1 and l-check(i)>=2:   #자음, 모음 조건 확인
            for j in range(l):
                print(i[j], end='')
            print(sep='\n')
