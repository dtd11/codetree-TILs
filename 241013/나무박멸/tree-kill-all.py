n,m,K,c = map(int,input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = 0
M = -10001
for i in range(n):
    for j in range(n):
        if arr[i][j] == -1:
            arr[i][j] = M #벽 최대한 작은 상수로 설정

for _ in range(m):
    #제초제 남은 년수 -
    for i in range(n):
        for j in range(n):
            if arr[i][j] < 0 and not arr[i][j] == M:
                arr[i][j] += 1

    #나무 성장
    for i in range(n):
        for j in range(n):
            if arr[i][j] > 0:
                cnt = 0
                for ni,nj in ((i-1,j),(i,j+1),(i+1,j),(i,j-1)):
                    if 0<=ni<n and 0<=nj<n and arr[ni][nj] > 0:
                        cnt += 1
                arr[i][j] += cnt
    #나무 번식
    narr = [x[:] for x in arr]
    for i in range(n):
        for j in range(n):
            if arr[i][j] > 0:
                cnt = 0
                lst = []
                for ni,nj in ((i-1,j),(i,j+1),(i+1,j),(i,j-1)):
                    if 0<=ni<n and 0<=nj<n and arr[ni][nj] == 0:
                        cnt += 1
                        lst.append((ni,nj))
                if cnt > 0:
                    for (ni, nj) in lst:
                        if arr[ni][nj] == 0:
                            narr[ni][nj] += arr[i][j] // cnt
    arr = [x[:] for x in narr]
    #제초제 위치 선정
    maxtree, mi, mj = 0, 0, 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] > 0:
                cnt = arr[i][j]
                for ni,nj in ((-1,-1),(-1,1),(1,1),(1,-1)):
                    for k in range(1, K+1):
                        nx,ny = i+k*ni, j+k*nj
                        if 0<=nx<n and 0<=ny<n and 0 < arr[nx][ny]:
                            cnt += arr[nx][ny]
                        else:
                            break
            if maxtree < cnt:
                maxtree, mi, mj = cnt, i, j
    #제초제 발포!
    narr = [x[:] for x in arr]
    narr[mi][mj] = -(c+1)
    for ni,nj in ((-1,-1),(-1,1),(1,1),(1,-1)):
        for k in range(1, K+1):
            nx,ny = mi+k*ni, mj+k*nj
            if 0 <= nx < n and 0 <= ny < n and 0 < arr[nx][ny]:
                narr[nx][ny] = -(c+1)
            elif 0 <= nx < n and 0 <= ny < n and arr[nx][ny] <= 0:
                if arr[nx][ny] == M:
                    break
                else:
                    narr[nx][ny] = -(c+1)
                    break
    arr = [x[:] for x in narr]
    ans += maxtree

print(ans)