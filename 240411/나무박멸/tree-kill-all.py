INF = -10001
n, m, k, c = map(int,input().split())
arr = [[INF]*(n+2)] + [[INF] + list(map(int, input().split())) + [INF] for _ in range(n)] + [[INF]*(n+2)]
c = -(c+1)
ans = 0

for i in range(1, n+1):
    for j in range(1, n+1):
        if arr[i][j] == -1:
            arr[i][j] = INF

for _ in range(m):
    # 시작
    for i in range(1, n+1):
        for j in range(1, n+1):
            if arr[i][j] < 0:
                arr[i][j] += 1
    # 나무 성장
    for i in range(1, n+1):
        for j in range(1, n+1):
            if arr[i][j] > 0:
                for ni, nj in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
                    if arr[ni][nj] > 0:
                        arr[i][j] += 1
    #나무 번식
    narr = [x[:] for x in arr]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if arr[i][j] > 0:
                tlst = []
                for ni, nj in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                    if arr[ni][nj] == 0:
                        tlst.append((ni, nj))
                if len(tlst) > 0:
                    for xi,xj in tlst:
                        narr[xi][xj] += arr[i][j] // len(tlst)
    arr = narr

    # 제초제를 뿌릴 위치 선정
    max, max_i, max_j = 0, 0, 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            if arr[i][j] > 0:
                sum = arr[i][j]
                for ci, cj in ((-1, -1), (-1, 1), (1, -1), (1, 1)):
                    for mul in range(1, k+1):
                        ni, nj = i + ci * mul, j + cj * mul
                        if arr[ni][nj] <= 0:
                            break
                        else:
                            sum += arr[ni][nj]
                if max < sum:
                    max, max_i, max_j = sum, i, j
    if max == 0:
        break
    ans += max

    #제초제 발포
    arr[max_i][max_j] = c
    for ci, cj in ((-1, -1), (-1, 1), (1, -1), (1, 1)):
        for mul in range(1, k + 1):
            ni, nj = max_i + ci * mul, max_j + cj * mul
            if arr[ni][nj] <= 0:
                if c <= arr[ni][nj]:
                    arr[ni][nj] = c
                break
            else:
                arr[ni][nj] = c

print(ans)