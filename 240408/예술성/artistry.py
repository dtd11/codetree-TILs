n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
m = n//2
from collections import deque

ans = 0

def bfs(si, sj):

    q = deque()

    q.append((si, sj))
    groups[-1].add((si, sj))
    v[si][sj] = 1

    while q:
        ci, cj = q.popleft()
        for ni, nj in ((ci-1, cj), (ci+1, cj), (ci, cj-1), (ci, cj+1)):
            if 0<=ni<n and 0<=nj<n and v[ni][nj] == 0 and arr[ci][cj] == arr[ni][nj]:
                q.append((ni, nj))
                v[ni][nj] = 1
                groups[-1].add((ni, nj))

for k in range(4):
    groups = [] #좌표값들 set으로 저장
    nums = [] #좌표 값의 값들 저장
    v = [[0]*n for _ in range(n)]
    # 그룹 나누기 및 좌표, 좌표값들 저장
    for i in range(n):
        for j in range(n):
            if v[i][j] == 0:
                groups.append(set())
                nums.append(arr[i][j])
                bfs(i, j)

    # 점수 합산
    cnt = len(nums)
    for i in range(cnt):
        for j in range(i+1, cnt):
            for ni, nj in groups[i]:
                for xi,xj in ((ni-1, nj), (ni+1, nj), (ni, nj-1), (ni, nj+1)):
                    if (xi,xj) in groups[j]:
                        ans += (len(groups[i])+len(groups[j])) * nums[i] * nums[j]

    #배열 회전
    if k == 3:
        break #3번돌면 그만

    narr = [[0]*n for _ in range(n)]
    for i in range(n):
        narr[i][m] = arr[m][n-1-i]
        narr[m][i] = arr[i][m]

    for ni, nj in ((0, 0), (0, m+1), (m+1, 0), (m+1, m+1)):
        for i in range(m):
            for j in range(m):
                narr[ni+i][nj+j] = arr[ni+m-1-j][nj+i]
    arr = narr

print(ans)