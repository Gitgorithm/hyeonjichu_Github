num=list(map(int, input().split()))
#증가하는 경우
if num[0]==1:
    i=1
    while i+1==num[i]:
        i+=1
        if i==8:
            print('ascending')
            break
    if i!=8:
        print('mixed')
#감소하는 경우
elif num[0]==8:
    i=7
    while i==num[8-i]:
        i-=1
        if i==0:
            print('descending')
            break
    if i!=0:
        print('mixed')
else:
    print('mixed')
