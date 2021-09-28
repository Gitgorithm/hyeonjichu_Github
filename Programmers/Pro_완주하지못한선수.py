def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(participant)):
        if i < len(completion) and participant[i] != completion[i]:
            answer = participant[i]
            break
        else:
            answer = participant[-1]
    return answer