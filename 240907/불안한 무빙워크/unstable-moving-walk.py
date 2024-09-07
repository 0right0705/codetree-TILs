n, k = map(int, input().split())
safety = list(map(int, input().split()))
mw = [[0] * 2 for  _ in range(n * 2)]
for i in range(len(mw)):
    mw[i][0] = safety[i]
zk = 0
cnt = 0

def simul():
    global zk
    global k
    #회전
    lastM = mw[n * 2 - 1][0]
    lastP = mw[n * 2 - 1][1]
    for i in range(len(mw) - 1, 0, -1):
        mw[i][0] = mw[i - 1][0]
        mw[i][1] = mw[i - 1][1]
    mw[0][0] = lastM
    mw[0][1] = lastP
    # print("rotate : ", mw)

    #0번 칸에 사람 올리기
    if mw[0][1] == 0 and mw[0][0] != 0:
        mw[0][1] = 1
        mw[0][0] -=1
    if mw[n - 1][0] == 0:
        zk += 1

    #앞으로 가기
    for i in range(n - 1, 1, -1):
        if mw[i][0] != 0 and mw[i][1] == 0:
            mw[i][1] = 1
            mw[i][0] -=1
            mw[i - 1][1] = 0
    if mw[n - 1][1] == 1:
        mw[n - 1][1] = 0
    if mw[n - 1][0] == 0:
        zk += 1
    
    #0번 칸에 사람 올리기
    if mw[0][1] == 0 and mw[0][0] != 0:
        mw[0][1] = 1
        mw[0][0] -=1
    if mw[n - 1][0] == 0:
        zk += 1
        return 0
    


while zk < k:
    simul()
    cnt += 1
print(cnt)