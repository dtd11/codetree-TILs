from collections import deque

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = 0
groups = []

def bfs(i, j):
    q = deque()
    q.append((i, j))
    groups.append(set())
    visited[i][j] = True
    while q:
        x, y = q.popleft()
        groups[-1].add((x, y))
        for dx, dy in ((-1,0),(1,0),(0,-1),(0,1)):
            nx, ny = x + dx, y + dy
            if nx > -1 and nx < n and ny > -1 and ny < n:
                if arr[x][y] == arr[nx][ny] and not visited[nx][ny]:
                    q.append((nx,ny))
                    groups[-1].add((nx,ny))
                    visited[nx][ny] = True

for _ in range(4):
    groups.clear()
    visited = [[False]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visited[i][j] == False:
                bfs(i,j)
    l = len(groups)
    cnt = 0
    for i in range(l):
        for j in range(i+1, l):
            for x,y in groups[i]:
                for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    nx, ny = x + dx, y + dy
                    if nx > -1 and nx < n and ny > -1 and ny < n:
                        if (nx,ny) in groups[j]:
                            cnt += (len(groups[i]) + len(groups[j])) * arr[x][y] * arr[nx][ny]
    ans += cnt

    m = n // 2
    narr = [[0]*n for _ in range(n)]

    for i in range(n):
        narr[m][i] = arr[i][m]
        narr[i][m] = arr[m][n-1-i]

    for i in range(m):
        for j in range(m):
            for di,dj in ((0,0),(m+1,0),(0,m+1),(m+1,m+1)):
                narr[i+di][j+dj] = arr[m-1-j+di][i+dj]
    arr = [a[:] for a in narr]

print(ans)