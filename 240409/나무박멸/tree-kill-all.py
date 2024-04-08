INF = -10000
n, m, k, c = map(int, input().split())
arr = [[INF]*(n+2)] + [[INF] + list(map(int, input().split())) + [INF] for _ in range(n)] + [[INF]*(n+2)]
c = -(c+1)
for i in range(1, n+1):
    for j in range(1, n+1):
        if arr[i][j] == -1:
            arr[i][j] = INF

ans = 0

for _ in range(m):
    #[0] 시작
    for i in range(1, n+1):
        for j in range(1, n+1):
            if arr[i][j] < 0:
                arr[i][j] += 1
    #[1] 성장
    narr = [x[:] for x in arr]
    for i in range(1, n+1):
        for j in range(1, n+1):
            if arr[i][j] > 0:
                for ni, nj in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
                    if arr[ni][nj] > 0:
                        narr[i][j] += 1
    arr = narr

    #[2] 번식
    narr = [x[:] for x in arr]
    for i in range(1, n+1):
        for j in range(1, n+1):
            if arr[i][j] > 0:
                tlst = []
                for ni, nj in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
                    if arr[ni][nj] == 0:
                        tlst.append((ni, nj))
                if len(tlst) > 0:
                    for xi, xj in tlst:
                        narr[xi][xj] += arr[i][j] // len(tlst)
    arr = narr
    #[3] 제초제 뿌릴 위치 선정
    max, max_i, max_j = 0, 0, 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            if arr[i][j] > 0:
                sum = arr[i][j]
                for ni, nj in ((-1, -1), (-1, 1), (1, -1), (1, 1)):
                    for mul in range(1, k+1):
                        xi, xj = i + ni * mul,  j + nj * mul
                        if arr[xi][xj] <= 0:
                            break
                        else:
                            sum += arr[xi][xj]
                if max < sum:
                    max, max_i, max_j = sum, i, j
    if max == 0:
        break
    ans += max

    #[4] 제초제 뿌리기
    arr[max_i][max_j] = c
    for ni, nj in ((-1, -1), (-1, 1), (1, -1), (1, 1)):
        for mul in range(1, k + 1):
            xi, xj = max_i + ni * mul, max_j + nj * mul
            if arr[xi][xj] <= 0:
                if c <= arr[xi][xj]:
                    arr[xi][xj] = c
                break
            else:
                arr[xi][xj] = c

print(ans)