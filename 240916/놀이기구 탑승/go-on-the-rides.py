n = int(input())
ride = [[0] * n for _ in range(n)]
students = [list(map(int, input().split())) for _ in range(n*n)]
student = students[0][0]
ride[n//2][n//2] = student

searchLike = [[-1,0],[1,0],[0,-1],[0,1]]

coords = []
visited =[]
likeStudent = [[0] *5 for _ in range(n)]
visited.append([n//2,n//2])
for number in range(1, n*n): #각각의 학생별로
    student = students[number][0] #0번째가 실제 학생 번호
    for i in range(n):  #y좌표
        for j in range(n): #x좌표
            for dx, dy in searchLike: #십자 탐색
                x = j + dx #x 이동
                y = i + dy #y이동
                if 0 <= x < n and 0 <= y < n and ([j, i] not in visited): #이동이 격자를 안벗어나면
                    for like in range(1, len(students[number])): #학생별로 좋아하는 학생 번호 탐색
                        if ride[x][y] == students[number][like]: #1~학생이 좋아하는 학생 수 까지 탐색하며 좋아하는 사람이 있다면
                            coords.append([j, i]) #좌표 배열에 좌표 넣기
    
    count_list=[]
    for coord in coords:
        count_list.append(coords.count(coord))
    if len(count_list) == len(coords) and (not len(coords) == 0): # 모두 같은 횟수라면
        ride[min(coords)[0]][min(coords)[1]] = student
        visited.append([min(coords)[0], min(coords)[1]])
    elif len(count_list) != len(coords) and (not (len(coords) == 0)): #max 값이 있다면
        index = 0
        index.append(coords.index(max(count_list)))
        ride[index[0]][index[1]] = student
    else:
        for i in range(n):
            for j in range(n):
                if [j,i] not in visited:
                    ride[j][i] = student
                    visited.append([j,i]) 
    coords.clear()
    count_list.clear()

ans = [0] * (n*n) 
for i in range(n):
    for j in range(n):
        member = ride[j][i]
        idx = 0
        for s in range(len(students)):
            if member == students[s][0]:
                idx = s
        for dx, dy in searchLike: #십자 탐색
            x = j + dx #x 이동
            y = i + dy #y이동
            if 0 <= x < n and 0 <= y < n:
                if ride[x][y] in students[idx]:
                    ans[member-1] += 1
sum = 0
for i in ans:
    if i == 0:
        sum +=  0
    elif i == 1:
        sum +=  1
    elif i == 2:
        sum += 10
    elif i == 3:
        sum += 100
    elif i == 4:
        sum += 1000
print(sum)