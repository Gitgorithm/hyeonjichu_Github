def solution(table, languages, preference):
    for i in range(len(table)):
        table[i] = table[i].split(' ')
        for j in range(1, 6):
            if table[i][j] in languages:
                idx = languages.index(table[i][j])
                table[i][j] = (6 - j) * preference[idx]
            else:
                table[i][j] = 0
        table[i].append(sum(table[i][1:]))
    table.sort(key=lambda x: (-int(x[6]), x[0]))

    return table[0][0]