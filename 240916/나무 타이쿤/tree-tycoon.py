def solve(trees, n, p, d, specials):
    dx, dy = d
    for i in range(len(specials)):
        specials[i][0], specials[i][1] = specials[i][0] + (dx*p), specials[i][1] + (dy*p)
        for j in range(2):
            if specials[i][j] < 0: specials[i][j] += n
            if specials[i][j] >= n: specials[i][j] = specials[i][j] % n
        trees[specials[i][0]][specials[i][1]] += 1
    for i in range(len(specials)):
        for tx, ty in [[-1,1], [-1,-1],[1,-1],[1,1]]:
            x,y = specials[i][0]+ tx, specials[i][1] + ty
            if 0<=x<n and 0<=y<n and trees[x][y]:
                trees[specials[i][0]][specials[i][1]] += 1
    cut = []
    for i in range(n):
        for j in range(n):
            if trees[i][j] >= 2 and ([i,j] not in specials):
                trees[i][j] -= 2
                cut.append([i,j])
    return cut

n, m = map(int, input().split())
trees = [list(map(int, input().split())) for _ in range(n)]
moves = [list(map(int, input().split())) for _ in range(m)]
directions = [(0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1)]
specials = [[n-1, 0], [n-1, 1], [n-2, 0], [n-2, 1]]
for d, p in moves:
    specials = solve(trees, n, p, directions[d-1], specials)
print(sum(sum(tree) for tree in trees))