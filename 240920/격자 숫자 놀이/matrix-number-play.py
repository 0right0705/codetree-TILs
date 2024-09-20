def play(board):
    cntarr = [] #count 담을 배열
    sortarr = []
    for i in range(len(board)): #열 탐색
        for j in range(len(board[i])): #행 탐색
            if board[i][j] != 0:
                cnt[0] = board[i][j]
                cnt[1] = board[i].count(board[i][j])
                cntarr.append([cnt[0], cnt[1]])
        cntarr = sorted(cntarr)
        cntarr = sorted(cntarr, key = lambda x :  (x[1], x[0]))
        for value in cntarr:
            if value not in sortarr:
                sortarr.append(value)
        board[i].clear()
        for value in sortarr:
            for j in value:
                board[i].append(j)
        sortarr.clear()
        cntarr.clear()
    lengths = []
    for i in board:
        lengths.append(len(i))
    maxlen = max(lengths)
    for i in range(len(lengths)):
        if lengths[i] < maxlen:
            for j in range(maxlen - lengths[i]):
                board[i].append(0)
    if len(board) > 100 or len(board[0]) > 100:
        newBoard = [[0]*100 for _ in range(100)]
        for i in range(100):
            for j in range(100):
                newBoard[i][j] = board[i][j] 
        board = newBoard
    return board

def rotate90(board,n,ret):
    for row in range(n):
        for column in range(len(board[row])):
            ret[column][n-1-row] = board[row][column]
    return ret

def makeRealWay(board,n, ret):
    for row in range(n):
        for column in range(len(board[row])):
            ret[column][n-1-row] = board[row][column]
    for i in range(len(ret)):
        ret[i] = ret[i][::-1]
    return ret

tr, tc, tk = map(int, input().split())
cnt = [0]*2 #0번째에는 숫자가, 1번째에는 빈도수가 들어가야함
board = [list(map(int,input().split())) for _ in range(3)]
tr -= 1
tc -= 1

r,c = 0,0
ans = 0
for turn in range(101):
    c = len(board[0])
    r = len(board)
    r -= 1
    c -= 1

    if 0<= tr< r and 0<=tc<c and board[tr][tc] == tk:
        ans = turn
        break

    if r >= c:
        n = len(board)
        ret = [[0] * n for _ in range(len(board[n-1]))]
        ret = play(board)
        board = ret
    elif r < c:
        n = len(board)
        ret = [[0] * n for _ in range(len(board[n-1]))]
        ret = rotate90(board, n, ret)
        board = ret
        ret = play(board)
        n = len(ret)
        ret1 = [[0] * n for _ in range(len(ret[n-1]))]
        ret1 = makeRealWay(ret,n,ret1)
        board = ret1
            
print(ans)