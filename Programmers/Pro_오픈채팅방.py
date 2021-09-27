def solution(record):
    answer = []
    id_nick = {}
    for i in range(len(record)):
        record[i] = list(record[i].split(' '))
        if record[i][0] != 'Leave':
            id_nick[str(record[i][1])] = str(record[i][2])
    for i in range(len(record)):
        if record[i][0] == 'Enter':
            answer.append(id_nick[record[i][1]] + '님이 들어왔습니다.')
        elif record[i][0] == 'Leave':
            answer.append(id_nick[record[i][1]] + '님이 나갔습니다.')

    return answer