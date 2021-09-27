def solution(s):
    answer = 10000
    word = list(s)
    for i in range(1, len(word)+1):
        tmp = [[0]]
        new_list = [word[j:j+i] for j in range(0, len(word),i)]
        cnt = 1
        for k in range(len(new_list)):
            if tmp[-1] != new_list[k]:
                tmp.append([str(cnt)])
                tmp.append(new_list[k])
                cnt = 1
            else:
                cnt += 1
            if k == len(new_list)-1:
                tmp.append([str(cnt)])
        del tmp[0]
        del tmp[0]
        tmp = sum(tmp,[])
        ans = 0
        for l in range(len(tmp)):
            if tmp[l] == "1":
                ans += 1
        answ = len(''.join(tmp))-ans
        answer = min(answer, answ)
    return answer