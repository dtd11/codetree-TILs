from collections import deque
from itertools import pairwise

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
m = n//2
ans = 0

def bfs(x,y):
    q = deque()

    q.append((x,y))
    groups[-1].append((x,y))
    visited[x][y] = True
    while q:
        cx, cy = q.popleft()
        for nx,ny in ((cx-1,cy), (cx,cy+1),(cx+1,cy),(cx,cy-1)):
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and arr[cx][cy] == arr[nx][ny]:
                q.append((nx,ny))
                groups[-1].append((nx,ny))
                visited[nx][ny] = True



for _ in range(4):
    groups = []
    nums = []
    visited = [[False]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                groups.append(list())
                nums.append(arr[i][j])
                bfs(i,j)
    cnt = len(nums)
    for i in range(cnt):
        for j in range(i+1, cnt):
            pnt = (len(groups[i])+ len(groups[j])) * nums[i] * nums[j]
            for ci,cj in groups[i]:
                for ni,nj in ((ci-1,cj),(ci,cj+1),(ci+1,cj),(ci,cj-1)):
                    if (ni,nj) in groups[j]:
                        ans += pnt

    narr = [x[:] for x in arr]
    for i in range(n):
        narr[m][i] = arr[i][m]
        narr[i][m] = arr[m][n-1-i]

    for i in range(m):
        for j in range(m):
            for si,sj in ((0,0),(m+1,0),(0,m+1),(m+1,m+1)):
                narr[si+i][sj+j] = arr[si+m-1-j][sj+i]
    arr = [x[:] for x in narr]


print(ans)