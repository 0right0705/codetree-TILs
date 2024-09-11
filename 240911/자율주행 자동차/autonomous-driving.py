import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


n, m = map(int, input().split())
x,y,d = map(int, input().split())
x, y = x, y #그래프는 0부터 시작하기 때문
d = 3 - d
graph = [list(map(int, input().split())) for _ in range(m)]
mx = [-1, 0, 1, 0] #서남동북
my = [0, 1, 0, -1] #서남동북
graph[x][y] = 2
cnt = 1

def solve(n,m,x,y,d,flag = 0):
    global cnt
    if flag == 4: #다 돌았는데 갈곳이 없을 시
        move_d = (d+2) % 4
        nx, ny = x + mx[move_d], y + my[move_d] #뒤로 가기
        if graph[nx][ny] == 1: #뒤로 갔을 때 갈 수 없는 곳이면
            return #리턴
        else: #갈 수 있는 곳이 있다면
            graph[nx][ny] = 2 #방문 표시 하기
            solve(n,m,nx,ny,d,0) #여기서 다시 1번부터 탐색하게 하기
    else: #아직 다 안돌았음
        move_d = (d+3) % 4 #왼쪽 방향으로 회전
        nx, ny = x + mx[move_d], y + my[move_d] #앞 칸으로 이동
        if graph[nx][ny] == 0: #앞칸이 비어있다면
            graph[nx][ny] = 2 #앞칸에 방문 표시 남기기
            cnt += 1 #방문된 칸 수 +1
            solve(n,m,nx,ny,move_d,0) #앞칸으로 이동해서 1번부터 다시 탐색
        else:
            solve(n,m,x,y,move_d, flag + 1) #같은 자리에서 flag + 1하며 탐색

solve(n,m,x,y,d,0)
print(cnt)