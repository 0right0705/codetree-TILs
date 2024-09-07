n, k = map(int, input().split())
safety = list(map(int, input().split()))
mw = [[0] * 2 for  _ in range(n * 2)]
for i in range(len(mw)):
    mw[i][0] = safety[i]
zk = 0

def Test1():
    lastM = mw[n * 2 - 1][0]
    lastP = mw[n * 2 - 1][1]
    for i in range(len(mw) - 1, 0, -1):
        mw[i][0] = mw[i - 1][0]
        mw[i][1] = mw[i - 1][1]
    mw[0][0] = lastM
    mw[0][1] = lastP
    mw[n - 1][1] = 0
    
    if mw[n-1][0] == 0:
        return 0

def Test2():
    mw[0][0] -= 1
    mw[0][1] = 1
    for i in range(n - 1, 1, -1):
        if mw[i][0] != 0 and mw[i][1] == 0:
            mw[i][1] = 1
            mw[i - 1][1] = 0
            mw[i  - 1][0] -= 1
    Test1()
    if mw[n-1][0] == 0:
        return 0

def Test3():
    if mw[0][1] == 0 and mw[0][0] != 0:
        mw[0][1] = 1
    Test1()
    if mw[n-1][0] == 0:
        return 0







while zk < k:
    if Test1() == 0:
        zk += 1
        if zk == k:
            print(1)
            break
    if Test2() == 0:
        zk += 1
        if zk == k:
            print(2)
            break
    if Test3() == 0:
        zk += 1
        if zk == k:
            print(3)
            break