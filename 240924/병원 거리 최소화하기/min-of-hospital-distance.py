n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
h = []
p = []
for x in range(n):
    for y in range(n):
        if graph[x][y] == 1:
            p.append([x, y])
        elif graph[x][y] == 2:
            h.append([x, y])

def comb(arr, n):
    result = []
    if n > len(arr):
        return result
    if n == 1:
        for i in arr:
            result.append([i])
    elif n > 1:
        for i in range(len(arr) - n + 1):
            for j in comb(arr[i+1:], n-1):
                result.append([arr[i]] + j)
    return result
hospital = comb(h, m)
ans = []
for i in hospital:
    d = 0
    for a in p:
        result = []
        for j in i:
            x, y = j[0], j[1]
            result.append(abs(a[0] - x) + abs(a[1] - y))
        d += sorted(result)[0]
    ans.append(d)
print(sorted(ans)[0])