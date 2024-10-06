from collections import deque

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
m = n // 2
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

ans = 0

def bfs(x, y):
    q = deque()

    q.append((x, y))
    groups[-1].add((x, y))
    visited[x][y] = True
    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and arr[cx][cy] == arr[nx][ny]:
                q.append((nx, ny))
                groups[-1].add((nx, ny))
                visited[nx][ny] = True

    #4번 회전
for k in range(4):
    groups = []
    nums = []
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                groups.append(set())
                nums.append(arr[i][j])
                bfs(i, j)


    cnt = len(nums)
    for i in range(cnt):
        for j in range(i+1, cnt):
            point = nums[i]*nums[j]*(len(groups[i]) + len(groups[j]))
            for (x, y) in groups[i]:
                for a in range(4):
                    nx, ny = x+dx[a], y+dy[a]
                    if (nx, ny) in groups[j]:
                        ans += point

    narr = [x[:] for x in arr]
    for i in range(n):
        narr[m][i] = arr[i][m]
        narr[i][m] = arr[m][n-1-i]

    for si, sj in ((0, 0), (0, m+1), (m+1, 0), (m+1, m+1)):
        for i in range(m):
            for j in range(m):
                narr[si+i][sj+j] = arr[si+m-1-j][sj+i]
    arr = narr

print(ans)