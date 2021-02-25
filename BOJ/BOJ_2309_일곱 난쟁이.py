data=[0]*9
for i in range(0,9):
    data[i]=int(input())
    
num=sum(data)-100
for i in range(0,9):
    n=data[i]
    data.remove(n)
    if num-n in data:
        data.remove(num-n)
        break
    else:
        data.insert(i,n)
    
data.sort()
for i in data:
    print(i, sep='\n')
