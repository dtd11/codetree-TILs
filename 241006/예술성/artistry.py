n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = 0
m = n // 2
from collections import deque

#bfs 수행
def bfs(si,sj):
    q = deque()

    q.append((si, sj))
    groups[-1].add((si, sj))
    v[si][sj] = 1

    while q:
        ci, cj = q.popleft()
        for ni,nj in ((ci-1,cj),(ci+1,cj),(ci,cj-1),(ci,cj+1)):
            if 0<=ni<n and 0<=nj<n and v[ni][nj] == 0 and arr[ci][cj] == arr[ni][nj]:
                q.append((ni,nj))
                groups[-1].add((ni,nj))
                v[ni][nj] = 1

for k in range(4):
    # bfs 시작 및 세팅
    groups = []  # 좌표 값들 저장
    nums = []    # 숫자 값 저장
    v = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if v[i][j] == 0:
                groups.append(set())
                nums.append(arr[i][j])
                bfs(i, j)
    # 점수 계산
    cnt = len(nums)
    for i in range(cnt):
        for j in range(i+1, cnt):
            point = (len(groups[i]) + len(groups[j])) * nums[i] * nums[j]
            for (ci, cj) in groups[i]:
                for ni, nj in ((ci-1, cj), (ci+1, cj), (ci, cj-1), (ci, cj+1)):
                    if (ni, nj) in groups[j]:
                        ans += point

    narr = arr
    for i in range(n):
        narr[m][i] = arr[i][m]
        narr[i][m] = arr[m][n-1-i]

    for si, sj in ((0,0),(0,m+1),(m+1,0),(m+1,m+1)):
        for i in range(m):
            for j in range(m):
                narr[si+i][sj+j] = arr[si+m-1-j][sj+i]
    arr = narr

print(ans)