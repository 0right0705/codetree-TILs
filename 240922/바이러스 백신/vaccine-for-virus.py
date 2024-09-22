from collections import deque
n, m = map(int, input().split())
board =[list(map(int, input().split())) for _ in range(n)]

findminarr = []
hospitals = []
dx =[0,0,-1,1]
dy = [-1,1,0,0]



for i in range(n):
    for j in range(n):
        if board[i][j] == 2:
            hospitals.append([i,j])

def bfs(selected):
    cnt = 0
    time = 0
    q = deque()
    visited = []
    answer = [[0]*n for _ in range(n)]
    for sx, sy in selected:
        q.append([sx, sy])
        visited.append([sx,sy])
    while q:
        i, j = q.popleft()
        for k in range(4):
            mx, my = dx[k] + i, dy[k] + j
            if 0<=mx<n and 0<=my<n :
                if board[mx][my] != 1:
                    if [mx, my] not in visited:
                        q.append([mx,my])
                        visited.append([mx,my])
                        if board[mx][my] == 2:
                            answer[mx][my] = answer[i][j]
                        elif board[mx][my] != 2: 
                            answer[mx][my] = answer[i][j] + 1


    for i in range(n):
        for j in range(n):
            if answer[i][j] == 0 and board[i][j] == 0:
                findminarr.append(-1) 
            else:
                time = max(time, answer[i][j])
    # for i in answer:
    #     print(i)
    #     time = max(time, max(i))
    # print("\n")
    findminarr.append(time)





def selectHospital(hospital, m):
    selected = []
    if len(hospital) < m:
        return selected
    if m == 1:
        for i in hospital:
            selected.append([i])
    elif m > 1:
        for i in range(len(hospital) - m + 1):
            for j in selectHospital(hospital[i+1:], m-1):
                selected.append([hospital[i]] + j)
    return selected
sh = selectHospital(hospitals, m)
for i in sh:
    bfs(i)
    
print(min(findminarr))