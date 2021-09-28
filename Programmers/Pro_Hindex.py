def solution(citations):
    for i in range(max(citations),-1,-1):
        list_len = len(list(filter(lambda x : x >= i, citations)))
        if i <= list_len:
            answer = i
            break
    return answer