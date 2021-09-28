def solution(genres, plays):
    answer = []
    key = [ x for x in range(len(genres))]
    music = list(map(list, zip(genres, plays, key)))
    music.sort(reverse=True, key = lambda x : (x[0], x[1]))
    #print(music)
    kind = []
    for i in range(len(music)):
        if len(kind) == 0 or music[i][0] != kind[-1][0]:
            kind.append([music[i][0], music[i][1], music[i][1], music[i][2]])
        else:
            kind[-1][1] += music[i][1]
            kind[-1].append(music[i][1])
            kind[-1].append(music[i][2])
    kind.sort(reverse=True, key = lambda x : x[1])
    #print(kind)
    for i in range(len(kind)):
        answer.append(kind[i][3])
        if len(kind[i]) >= 6:
            answer.append(kind[i][5])

    return answer