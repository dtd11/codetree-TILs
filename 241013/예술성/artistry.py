from collections import deque

n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
ans = 0

def bfs(i,j):
    q = deque()
    q.append((i,j))
    groups[-1].add((i,j))
    visited[i][j] = True

    while q:
        ci, cj = q.popleft()
        for (ni,nj) in ((ci-1,cj),(ci,cj+1),(ci+1,cj),(ci,cj-1)):
            if 0<=ni<n and 0<=nj<n and not visited[ni][nj] and arr[ci][cj]==arr[ni][nj]:
                q.append((ni,nj))
                groups[-1].add((ni,nj))
                visited[ni][nj]=True

for _ in range(4):
    groups = [] #좌표 저장
    nums = [] #좌표 값 저장
    visited =[[False]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                groups.append(set())
                nums.append(arr[i][j])
                bfs(i, j)
    cnt = len(nums)
    for i in range(cnt):
        for j in range(i+1, cnt):
            pnt = (len(groups[i]) + len(groups[j])) * nums[i] * nums[j]
            for (x,y) in groups[i]:
                for (nx,ny) in ((x-1,y),(x,y+1),(x+1,y),(x,y-1)):
                    if (nx,ny) in groups[j]:
                        ans += pnt

    narr = [x[:] for x in arr]
    m = n//2
    for i in range(n):
        narr[i][m] = arr[m][n-1-i]
        narr[m][i] = arr[i][m]

    for (ni,nj) in ((0,0),(m+1,0),(0,m+1),(m+1,m+1)):
        for i in range(m):
            for j in range(m):
                narr[ni+i][nj+j] = arr[ni+m-1-j][nj+i]
    arr = [x[:] for x in narr]
print(ans)