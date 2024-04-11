n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
# 참가자 좌표 값 받기
for _ in range(m):
    mi, mj = map(lambda x: int(x)-1, input().split())
    arr[mi][mj] = -1 # 사람 -1로

ei, ej = map(lambda x: int(x)-1, input().split())
arr[ei][ej] = -111 # 출구 -111로 취급

ans = 0 # 이동거리 합
cnt = m # 탈출한 사람 명수(0되면 종료)

def find_square(arr):
    L = n
    for i in range(n):
        for j in range(n):
            if -111 < arr[i][j] < 0:
                L = min(L, max(abs(ei-i), abs(ej-j)))

    for i in range(n-L):
        for j in range(n-L):
            if i<=ei<=i+L and j<=ej<=j+L:
                for si in range(i, i+L+1):
                    for sj in range(j, j+L+1):
                        if -111 < arr[si][sj] < 0:
                            return i, j, L+1

def find_exit(arr):
    for i in range(n):
        for j in range(n):
            if arr[i][j] <= -111:
                return i, j

for _ in range(k):
    # 참가자 이동
    narr = [x[:] for x in arr]
    for i in range(n):
        for j in range(n):
            if -111 < arr[i][j] < 0:
                dist = abs(ei-i) + abs(ej-j)
                for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    ni, nj = i+di, j+dj
                    if 0<=ni<n and 0<=nj<n and arr[ni][nj] <=0 and dist > (abs(ei-ni) + abs(ej-nj)):
                        ans -= arr[i][j] # 참가자 이동거리
                        narr[i][j] -= arr[i][j] # 이동처리
                        if arr[ni][nj] <= -111:
                            cnt += arr[i][j] #참가자들 탈출!
                        else:
                            narr[ni][nj] += arr[i][j]
                        break
    arr = narr

    if cnt == 0:
        break

    si, sj, L = find_square(arr)
    narr = [x[:] for x in arr]
    for i in range(L):
        for j in range(L):
            narr[si+i][sj+j] = arr[si+L-1-j][sj+i]
            if narr[si+i][sj+j] > 0:
                narr[si + i][sj + j] -= 1
    arr = narr
    ei, ej = find_exit(arr)

print(ans)
print(ei+1, ej+1)