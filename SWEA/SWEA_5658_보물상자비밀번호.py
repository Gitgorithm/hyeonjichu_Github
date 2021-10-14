T = int(input())
for test_case in range(1, T + 1):
    answer = []
    n, k = map(int, input().split())
    num = list(input())

    for j in range(int(n / 4)):
        str = ''
        tmp = num[0]
        del num[0]
        num.append(tmp)
        for i in range(n):
            if i == n - 1:
                str += num[i]
                answer.append(int('0x' + str, 16))
                break
            if i != 0 and i % int(n / 4) == 0:
                answer.append(int('0x' + str, 16))
                str = num[i]
            else:
                str += num[i]
    answer.sort(reverse=True)
    answer = list(set(answer))
    print('#%d' % test_case, answer[k - 1])