sum=int(input()) #ex)sum=55 => n=10
n=0
for i in range(1, sum, +1):
    n+=i
    if n>=sum:
        print(i)
        break
