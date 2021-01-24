a=input()
for i in range(len(a)):
    print('['+str(int(a[i])*(10**(len(a)-(i+1))))+']')
