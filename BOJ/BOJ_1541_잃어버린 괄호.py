data = list(input().split('-'))
result = 0
if len(data) == 1:
    data = data[0].split("+")
    result += sum(map(int, data))
else:
    result += sum(list(map(int,data[0].split("+"))))
    for i in range(1, len(data)):
        if "+" in data[i]:
            result -= sum(list(map(int, data[i].split("+"))))
        else:
            result -= int(data[i])
print(result)