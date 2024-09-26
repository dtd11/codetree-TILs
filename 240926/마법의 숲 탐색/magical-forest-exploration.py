from collections import deque

R, C, K = 0, 0, 0
Max_L = 70
dx = [1,0,-1,0]
dy = [0,1,0,-1]
Map = [[0]*Max_L for _ in range(Max_L+3)]
isExit = [[False]*Max_L for _ in range(Max_L+3)]
answer = 0
# 짜야될 함수 : 범위안, 글로 갈수 있는지, bfs탐색해서 행 값 리턴, 아래로 이동하는 탐색 함수
# 범위안에 있는지
def isRange(x,y):
    return 3 <= x < R+3 and 0 <= y < C

def resetMap():
    for i in range(R + 3):
        for j in range(C):
            Map[i][j] = 0
            isExit[i][j] = False

# 위에서 아래로 한 칸갈 수 있는지 확인하는 함수 (x-1,y) -> (x,y)
def canGo(x,y):
    flag = x < R + 2 and 1 <= y < C - 1
    flag = flag and (Map[x - 1][y]==0)
    flag = flag and (Map[x - 1][y - 1] == 0)
    flag = flag and (Map[x - 1][y + 1] == 0)
    flag = flag and (Map[x][y] == 0)
    flag = flag and (Map[x][y - 1] == 0)
    flag = flag and (Map[x][y + 1] == 0)
    flag = flag and (Map[x + 1][y] == 0)
    return flag

#bfs로 갈수 잇는지 없는지 파악
def bfs(x,y):
    result = x
    q = deque([x,y])
    visited = [[False]*C for _ in range(R+3)]
    visited[x][y] = True

    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if isRange(nx, ny) and not visited[ny][nx] and (Map[nx][ny] == Map[cx][cy] or (Map[nx][ny] != 0 and isExit[cx][cy])):
                q.append((nx,ny))
                visited[nx][ny] = True
                result = max(result, x)
    return result


# 아래로 이동
def goDown(x,y,d,k):
    if canGo(x+1,y): # 아래로 한 칸 이동
        goDown(x+1,y,d,k)
    elif canGo(x+1,y-1): # 왼쪽으로 한 번 구르기
        goDown(x+1,y-1,(d+3)%4, k)
    elif canGo(x+1,y+1): # 오른쪽으로 한 번 구르기
        goDown(x+1,y+1,(d+1)%4, k)
    else:
        if isRange(x-1, y-1) and isRange(x+1, y+1):
            Map[x][y] = k
            for i in range(4):
                Map[x+dx[i]][y+dy[i]] = k
                isExit[x+dx[d]][y+dy[d]] = True
                global answer
                answer += bfs(x,y) - 2
        else:
            resetMap()

def main():
    global R,C,K
    R,C,K = map(int, input().split())
    for k in range(2,K+2):
        y, d = map(int, input().split())
        goDown(0, y-1, d, k)
    print(answer)
    
if __name__ == "__main__":
    main()