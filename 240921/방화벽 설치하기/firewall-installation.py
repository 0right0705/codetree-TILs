from collections import deque
dx = [0,0,-1,1]
dy = [1,-1,0,0]
visited = []
def deepcopy(original):
    return [row[:] for row in original]
def bfs():
    visited = deepcopy(arr)
    queue = deque()
    for i in range(n):
        for j in range(m):
            if visited[i][j] == 2:
                queue.append((i,j))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if visited[nx][ny] == 0:
                visited[nx][ny] = 2
                queue.append((nx, ny))
    global answer
    cnt = 0
    for i in range(n):
        cnt += visited[i].count(0)
    answer = max(answer, cnt)
        


def makewall(cnt):
    if cnt == 3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                arr[i][j] = 1
                makewall(cnt+1)
                arr[i][j] = 0
    

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

answer = 0
makewall(0)
print(answer)