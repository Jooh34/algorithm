def solution(commands):
    table = []
    for i in range(51):
        row = []
        for j in range(51):
            cell = [set([(i,j)]), "EMPTY"]
            row.append(cell)
        
        table.append(row)

    def update(i, j, value):
        for x,y in table[i][j][0]:
            table[x][y][1] = value
    
    def replace(i, j, value):
        table[i][j] = [set([(i,j)]), value]

    answer = []
    for comm in commands:
        s = comm.split()
        if s[0] == "UPDATE":
            if len(s) == 4:
                _, r, c, value = s
                update(int(r),int(c),value)

            else:
                _, value1, value2 = s 
                for i in range(1,51):
                    for j in range(1,51):
                        if table[i][j][1] == value1:
                            table[i][j][1] = value2
        
        elif s[0] == "MERGE":
            r1, c1, r2, c2 = map(int, s[1:])
            value = table[r2][c2][1] if table[r1][c1][1] == "EMPTY" else table[r1][c1][1]
            if value == "EMPTY":
                value = table[r2][c2][1]
            
            table[r1][c1][0] |= table[r2][c2][0]
            for x,y in table[r1][c1][0]:
                table[x][y][0] = table[r1][c1][0]
                table[x][y][1] = value
        
        elif s[0] == "UNMERGE":
            r, c = map(int, s[1:])
            value = table[r][c][1]
            for x,y in table[r][c][0]:
                if r == x and c == y: continue
                replace(x,y,"EMPTY")
            
            replace(r,c,value)
        
        else: # PRINT
            r, c = map(int, s[1:])
            answer.append(table[r][c][1])

    return answer

q1 = ["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"]
print(solution(q1))