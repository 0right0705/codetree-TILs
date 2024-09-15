tf1 = input()
tf2 = input()
tf3 = input()
tf4 = input()
t1,t2,t3,t4 = [],[],[],[]
for i in tf1:
    t1.append(int(i))
for i in tf2:
    t2.append(int(i))
for i in tf3:
    t3.append(int(i))
for i in tf4:
    t4.append(int(i))
table = []
table.append(t1)
table.append(t2)
table.append(t3)
table.append(t4)

def rotate(n, way):
    if way == 1: #시계방향 회전
        last = table[n][7] #table의 마지막 값 저장
        for i in range(7, 0, -1):
            table[n][i] = table[n][i - 1]
        table[n][0] = last
    if way == -1: #반시계방향 회전
        first = table[n][0]
        for i in range(0, 7):
            table[n][i] = table[n][i + 1]
        table[n][7] = first

def checkLeft(n): #n번째의 왼쪽 테이블 돌릴지 말지 체크
    if table[n][6] != table[n-1][2]:   
        return True
    else:
        return False

def checkRight(n): #n번쨰의 오른쪽 테이블 돌릴지 말지 체크
    if table[n][2] != table[n+1][6]:
        return True
    else:
        return False 

tc = int(input())
for z in range(tc):
    
    n, k = map(int, input().split())
    n -= 1

    #여기부터 회전하고 확인하는 코드 채우기
    rt = []


    if n == 0:
        if checkLeft(n+1) == True or checkRight(n-1):
            rt.append([n, k])
        if checkRight(0) == True:
            rt.append([1, -k])
        if checkRight(n+1) == True:
            rt.append([n+2, k])
        if checkRight(n+2) == True:
            rt.append([n+3, -k])

    if n == 4:
        if checkLeft(n+1) == True or checkRight(n-1):
            rt.append([n, k])
        if checkRight(n) == True:
            rt.append([n-1, -k])
        if checkRight(n+1) == True:
            rt.append([n-2, k])
        if checkRight(n+2) == True:
            rt.append([n-3, -k])
    if n == 1:
        if checkLeft(n+1) == True or checkRight(n-1):
            rt.append([n, k])
        if checkLeft(n) == True:
            rt.append([n-1,-k])
        if checkRight(n) == True:
            rt.append([n+1,-k])
        if checkRight(n+1) == True:
            rt.append([n+2,k])
    if n == 2:
        if checkLeft(n+1) == True or checkRight(n-1):
            rt.append([n, k])
        if checkLeft(n) == True:
            rt.append([n-1,-k])
        if checkLeft(n-1) == True:
            rt.append([n-2, k])
        if checkRight(n) == True:
            rt.append([n+1,-k])
    for rotation in rt:
        rotate(rotation[0], rotation[1])

s1,s2,s3,s4 = table[0][0], table[1][0], table[2][0], table[3][0]
print(1*s1 + 2*s2 + 4*s3 + 8*s4)