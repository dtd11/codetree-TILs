INF = -10000
n, m, k, c = map(int, input().split())
# 벽처리를 땅의 겉을 INF로 둘러싸서 처리해줌
arr = [[INF]*(n+2)] + [[INF] + list(map(int, input().split())) + [INF] for _ in range(n)] + [[INF]*(n+2)]
c = -(c+1) # c+1에 딱 제초제가 사라져야 함
for i in range(1, n+1):
    for j in range(1, n+1):
        if arr[i][j] == -1:
            arr[i][j] = INF

ans = 0 #정답 값

#m년동안 진행
for _ in range(m):
    #[0] 새해의 시작
    for i in range(1, n+1):
        for j in range(1, n+1):
            if arr[i][j] < 0:
                arr[i][j] += 1

    #[1] 나무의 성장
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if arr[i][j] > 0:  # 나무가 있다면, 인접 나무수만큼 성장
                for ni, nj in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                    if arr[ni][nj] > 0:
                        arr[i][j] += 1


    #[2] 나무의 번식
    narr = [x[:] for x in arr]
    for i in range(1, n+1):
        for j in range(1, n+1):
            if arr[i][j] > 0:
                tlst = []
                for ni, nj in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
                    if arr[ni][nj] == 0:
                        tlst.append((ni, nj))
                if len(tlst) > 0:
                    s = arr[i][j] // len(tlst)
                    for xi, xj in tlst:
                        narr[xi][xj] += s
    arr = narr

    #[3] 가장 많이 박멸되는 칸 찾기
    max, max_i, max_j = 0, 0, 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            if arr[i][j] > 0:
                sum = arr[i][j]
                for ni, nj in ((-1, -1), (-1, 1), (1, -1), (1, 1)):
                    for mul in range(1, k+1):
                        xi, xj = i + mul * ni, j + mul * nj
                        if arr[xi][xj] <= 0:
                            break
                        else:
                            sum += arr[xi][xj]
                if max < sum:
                    max, max_i, max_j = sum, i, j
    if max == 0:
        break
    ans += max

    #[4] 박멸
    arr[max_i][max_j] = c
    for ni, nj in ((-1, -1), (-1, 1), (1, -1), (1, 1)):
        for mul in range(1, k+1):
            xi, xj = max_i + mul * ni, max_j + mul * nj
            if arr[xi][xj] <= 0:
                if c <= arr[xi][xj]:
                    arr[ni][nj] = c
                break
            else:
                arr[ni][nj] = c
print(ans)