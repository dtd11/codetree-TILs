n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
for _ in range(m):
    i, j = map(int, input().split())
    arr[i-1][j-1] = -1 # 인간 -1로 처리, 점수처리 잘하기위해서
ei, ej = map(int, input().split())
arr[ei-1][ej-1] = -111 # 출구 -111로 처리
ei -= 1
ej -= 1
ans = 0
cnt = m
# 출구
def find_square(arr):
    # 가장 작은 정사각형 한 변의 길이 찾기
    L = n
    for i in range(n):
        for j in range(n):
            if -111 < arr[i][j] < 0: #사람이면
                L = min(L, max(abs(ei-i), abs(ej-j)))

    for si in range(n-L):
        for sj in range(n-L):
            if si<=ei<=si+L and sj<=ej<=sj+L:
                for i in range(si, si+L+1):
                    for j in range(sj, sj+L+1):
                        if -111 < arr[i][j] < 0:
                            return si,sj,L+1
# 출구 좌표값 찾기
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
                for ni,nj in ((i-1,j), (i+1, j), (i, j-1), (i, j+1)):
                    if 0<=ni<n and 0<=nj<n and arr[ni][nj] <= 0 and (abs(ei-ni) + abs(ej - nj)) < dist:
                        ans -= arr[i][j]
                        narr[i][j] -= arr[i][j]
                        if arr[ni][nj] <= -111:
                            cnt += arr[i][j]
                        else:
                            narr[ni][nj] += arr[i][j]
                        break
    arr = narr
    if cnt == 0:
        break

    xi,xj,mn = find_square(arr)
    narr = [x[:] for x in arr]
    for i in range(mn):
        for j in range(mn):
            narr[xi+i][xj+j] = arr[xi+mn-1-j][xj+i]
            if narr[xi+i][xj+j] > 0:
                narr[xi+i][xj+j] -= 1
    arr = narr

    ei, ej = find_exit(arr)

print(ans)
print(ei+1, ej+1)