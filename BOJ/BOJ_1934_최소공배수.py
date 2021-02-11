num=int(input())
def gcd(a,b):
    if a<b:
        (a,b)=(b,a)
    while a%b!=0:
        (a,b)=(b,a%b)
    return b
    
def lcm(a,b):
    c=gcd(a,b)
    return int(a*b/c)

for i in range(num):
    a,b=map(int,input().split())
    print(lcm(a,b))
