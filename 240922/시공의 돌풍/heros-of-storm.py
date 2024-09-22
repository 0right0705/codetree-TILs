n, m, t = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(n)]
mdx = [0,1,0,-1]
mdy = [1,0,-1,0]

winds = []
sec = 0
for i in range(n):
    if room[i][0] == -1:
        winds.append(i)
while True:
    dustroom = [[0] * m for _ in range(n)]
    cleanroom = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if room[i][j] > 0:
                dust = room[i][j] // 5
                for k in range(4):
                    mx, my = mdx[k] + i, mdy[k] + j
                    if 0<=mx<n and 0<=my<m and room[mx][my] != -1:
                        dustroom[mx][my] += dust
                        room[i][j] -= dust
                
    for i in range(n):
        for j in range(m):
            if room[i][j] != -1:
                room[i][j] += dustroom[i][j]
    # 윗쪽 반시계 방향 순환
    uy = winds[0]
    for i in range(uy - 1, 0, -1):
        room[i][0] = room[i - 1][0]
    for i in range(m - 1):
        room[0][i] = room[0][i + 1]
    for i in range(uy):
        room[i][m - 1] = room[i + 1][m - 1]
    for i in range(m - 1, 1, -1):
        room[uy][i] = room[uy][i - 1]
    room[uy][1] = 0  # 청정기에서 나오는 공기는 먼지가 없음

    # 아랫쪽 시계 방향 순환
    dy = winds[1]
    for i in range(dy + 1, n - 1):
        room[i][0] = room[i + 1][0]
    for i in range(m - 1):
        room[n - 1][i] = room[n - 1][i + 1]
    for i in range(n - 1, dy, -1):
        room[i][m - 1] = room[i - 1][m - 1]
    for i in range(m - 1, 1, -1):
        room[dy][i] = room[dy][i - 1]
    room[dy][1] = 0  # 청정기에서 나오는 공기는 먼지가 없음


    for i in range(n):
        for j in range(m):
            if cleanroom[i][j] != 0:
                room[i][j] = cleanroom[i][j]
    room[uy][1] = 0
    room[dy][1] = 0


    sec += 1
    if sec == t:
        break

cnt = 0
for i in room:
    cnt += sum(i)
cnt += 2
print(cnt)