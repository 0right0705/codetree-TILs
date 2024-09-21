n,m,x,y,k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
way = list(map(int, input().split()))
dice = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

def east():
    global x,y,graph

    if x + 1 >= m:
        return False
    else:
        x += 1

        if graph[y][x] == 0:
            dice[4][1] = dice[2][1]
            dice[2][1] = dice[2][2]
            dice[2][2] = dice[2][3]
            dice[2][3] = dice[4][2]
            dice[4][2] = dice[4][1]
            graph[y][x] = dice[2][2]
            dice[4][1] = 0
        else:
            dice[4][1] = dice[2][1]
            dice[2][1] = dice[2][2]
            dice[2][2] = dice[2][3]
            dice[2][3] = dice[4][2]
            dice[4][2] = dice[4][1]
            dice[4][1] = 0
            dice[2][2] = graph[y][x]
            graph[y][x] = 0

        return [y,x]

def west():
    global x,y,graph
    if x-1 < 0:
        return False
    else:
        x -= 1
        if graph[y][x] == 0:
            dice[4][1] = dice[2][3]
            dice[2][3] = dice[2][2]
            dice[2][2] = dice[2][1]
            dice[2][1] = dice[4][2]
            dice[4][2] = dice[4][1]
            graph[y][x] = dice[2][2]
            dice[4][1] = 0
        else:
            dice[4][1] = dice[2][3]
            dice[2][3] = dice[2][2]
            dice[2][2] = dice[2][1]
            dice[2][1] = dice[4][2]
            dice[4][2] = dice[4][1]
            dice[2][2] = graph[y][x]
            dice[4][1] = 0
            graph[y][x] = 0

        return [y,x]

def north():
    global x,y,graph
    if y-1 < 0:
        return False
    else:
        y -= 1
        if graph[y][x] == 0:
            dice[0][2] = dice[4][2]
            dice[4][2] = dice[3][2]
            dice[3][2] = dice[2][2]
            dice[2][2] = dice[1][2]
            dice[1][2] = dice[0][2]
            graph[y][x] = dice[2][2]
            dice[0][2] = 0
        else:
            
            dice[0][2] = dice[4][2]
            dice[4][2] = dice[3][2]
            dice[3][2] = dice[2][2]
            dice[1][2] = dice[0][2]
            dice[2][2] = graph[y][x]
            graph[y][x] = 0
            dice[0][2] = 0

        return [y,x]

def south():
    global x, y, graph
    if y+1>= n:
        return False
    else:
        y += 1
        if graph[y][x] == 0:
            dice[5][2] = dice[1][2]
            dice[1][2] = dice[2][2]
            dice[2][2] = dice[3][2]
            dice[3][2] = dice[4][2]
            dice[4][2] = dice[5][2]
            graph[y][x] = dice[2][2]
            dice[5][2] = 0
        else:
            dice[5][2] = dice[1][2]
            dice[1][2] = dice[2][2]
            dice[3][2] = dice[4][2]
            dice[4][2] = dice[5][2]
            dice[2][2] = graph[y][x]
            graph[y][x] = 0
            dice[5][2] = 0

        return [y,x]

for i in way:
    
    if i == 1:
        result = east()
        if result != False:
            print(dice[4][2])
    elif i == 2:
        result = west()
        if result != False:
            print(dice[4][2])
    elif i == 3:
        result = north()
        if result != False:
            print(dice[4][2])
    else:
        result = south()
        if result != False:
            print(dice[4][2])