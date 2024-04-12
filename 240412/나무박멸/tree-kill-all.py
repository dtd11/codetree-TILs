INF = -10000
n, m, k, c = map(int, input().split()) #격자크기, 박멸 진행 년수, 제초제 확산 범위, 제초제 남아있는 년 수
arr = [[INF]*(n+2)] + [[INF] + list(map(int, input().split())) + [INF] for _ in range(n)] + [[INF]*(n+2)] #배열 입력받기
c = -(c+1)
# 배열에서 겉부분을 벽으로 둘러싸서 편하게 세팅해줌
for i in range(1, n+1):
    for j in range(1, n+1):
        if arr[i][j] < 0:
            arr[i][j] = INF
# 정답값
ans = 0
# m년동안 진행
for _ in range(m):
    # 시작
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if arr[i][j] < 0:
                arr[i][j] += 1 #제초제 1년 증가

    # 나무의 성장
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if arr[i][j] > 0:
                for ni, nj in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
                    if arr[ni][nj] > 0:
                        arr[i][j] += 1
    # 나무의 번식
    narr = [x[:] for x in arr]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if arr[i][j] > 0:
                tlst = []
                for ni, nj in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
                    if arr[ni][nj] == 0:
                        tlst.append((ni, nj))
                if len(tlst) > 0:
                    for xi, xj in tlst:
                        narr[xi][xj] += arr[i][j] // len(tlst)
    arr = narr
    # 제초제 뿌릴 위치 선정
    mx, mx_i, mx_j = 0, 0, 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if arr[i][j] > 0:
                sum = arr[i][j]
                for di,dj in ((-1,-1),(-1,1),(1,-1),(1,1)):
                    for m in range(1,k+1):
                        ni, nj = i+m*di, j+m*dj
                        if arr[ni][nj] <= 0:
                            break
                        else:
                            sum += arr[ni][nj]
                if mx < sum:
                    mx, mx_i, mx_j = sum, i, j
    if mx == 0:
        break
    ans += mx

    # 제초제 발포
    arr[mx_i][mx_j] = c
    for di, dj in ((-1, -1), (-1, 1), (1, -1), (1, 1)):
        for m in range(1, k + 1):
            ni, nj = mx_i+m*di, mx_j+m*dj
            if arr[ni][nj] <= 0:
                if c <= arr[ni][nj]:
                    arr[ni][nj] = c
                break
            elif arr[ni][nj] > 0:
                arr[ni][nj] = c

print(ans)