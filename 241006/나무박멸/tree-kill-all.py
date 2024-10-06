from collections import deque

#격자크기, 박멸진행년수, 제초제 확산범위, 제초제 남아있는 년 수
n, m, k, c = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = 0

for i in range(n):
    for j in range(n):
        if arr[i][j] == -1:
            arr[i][j] = -10000 #벽이면 -10000로 초기화


for _ in range(m):
    #제초제 남은 년수 1년 줄이기
    for i in range(n):
        for j in range(n):
            if arr[i][j] < 0 and not arr[i][j] == -10000:
                arr[i][j] += 1
    # 나무 성장
    for i in range(n):
        for j in range(n):
            if arr[i][j] > 0:
                for ni,nj in ((i-1,j),(i,j+1),(i+1,j),(i,j-1)):
                    if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] > 0:
                        arr[i][j] += 1

    # 번식
    narr = [x[:] for x in arr]
    for i in range(n):
        for j in range(n):
            if arr[i][j] > 0:
                cnt = 0
                xy = []
                for ni, nj in ((i-1,j),(i,j+1),(i+1,j),(i,j-1)):
                    if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] == 0:
                        cnt += 1
                        xy.append((ni, nj))
                if cnt > 0:
                    for (x, y) in xy:
                        narr[x][y] += arr[i][j] // cnt
    arr = [x[:] for x in narr]

    max, max_i, max_j = 0, 0, 0
    #제초제 위치 선정
    for i in range(n):
        for j in range(n):
            if arr[i][j] > 0:
                sum = arr[i][j]
                for di,dj in ((-1,-1), (-1, 1), (1,-1), (1,1)):
                    for mul in range(1, k+1):
                        ni, nj = i + mul * di, j + mul * dj
                        if 0<=ni<n and 0<=nj<n and arr[ni][nj] > 0:
                            sum += arr[ni][nj]
                        else:
                            break
                if sum > max:
                    max, max_i, max_j = sum, i, j
    #제초
    arr[max_i][max_j] = -(c+1)
    for di,dj in ((-1,-1), (-1,1), (1,-1), (1,1)):
        for mul in range(1, k+1):
            ni, nj = max_i + mul * di, max_j + mul * dj
            if 0 <= ni < n and 0 <= nj < n and (arr[ni][nj] > 0 or arr[ni][nj] >= -(c+1)):
                arr[ni][nj] = -(c+1)
            else:
                break
    ans += max

print(ans)