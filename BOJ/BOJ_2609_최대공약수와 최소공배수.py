a,b=map(int, input().split())
def gcd(a,b):
    if a<b:
        (a,b)=(b,a)
    while a%b != 0:
        (a,b)=(b,a%b)
    return b
def lcm(a,b):
    c=gcd(a,b)
    return int(a*b/c)
print(gcd(a,b)) #최대공약수
print(lcm(a,b)) #최소공배수
    
