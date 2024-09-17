n = int(input())
ride = [[0] * n for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
likegrid =[[[] for _ in range(n)] for _ in range(n)]
for _ in range(n*n):
    now, l1,l2,l3,l4 = map(int, input().split())
    like = [l1,l2,l3,l4]
    candidate = []

    for i in range(n):
        for j in range(n):
            if ride[i][j] != 0:
                continue
            likecnt, emptycnt = 0,0
            for search in range(4):
                mx, my = dx[search] + i, dy[search] + j
                if (0<=mx<n) and (0<=my<n ):
                    if ride[mx][my] in like:
                        likecnt += 1
                    if ride[mx][my] == 0:
                        emptycnt += 1
                    candidate.append([likecnt, emptycnt, i, j])
    candidate.sort(key = lambda x:(-x[0], -x[1], x[2], x[3]))
    r,c = candidate[0][2], candidate[0][3]
    ride[r][c] = now
    likegrid[r][c] = like
ans = 0
for i in range(n):
    for j in range(n):
        point = 0
        for search in range(4):
            mx, my = dx[search]+i, dy[search]+j
            if (0<=mx<n) and (0<=my<n):
                if ride[mx][my] in likegrid[i][j]:
                    point += 1
        if point == 1:
            ans += 1
        elif point == 2:
            ans += 10
        elif point == 3:
            ans += 100
        elif point == 4:
            point += 1000
print(ans)