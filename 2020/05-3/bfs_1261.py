# 1261
from collections import deque

ARR_MAX = 10001
da = [0, 0, 1, -1]
db = [-1, 1, 0, 0]

def BFS(N, M, arr, visited):
    deq = deque()
    deq.append([0, 0])
    visited[0][0] = 0
    while(len(deq)):
        fnt = deq.popleft()
        ca = fnt[0]
        cb = fnt[1]
        # print(fnt)
        for dir in range(0, 4):
            na = ca + da[dir]
            nb = cb + db[dir]
            if na < 0 or na >= M or nb < 0 or nb >= N:
                continue
            if arr[na][nb] == '0' and visited[na][nb] > visited[ca][cb]:
                visited[na][nb] = visited[ca][cb]
                deq.append([na, nb])
            if arr[na][nb] == '1' and visited[na][nb] > visited[ca][cb] + 1:
                visited[na][nb] = visited[ca][cb] + 1
                deq.append([na, nb])
    # for i in range(0, M):
    #     print(visited[i])
    return visited[M - 1][N - 1]

if __name__ == "__main__":
    N, M = map(int, input().split())
    arr = []
    visited = []
    for i in range(0, M):
        arr.append(list(input()))
        tmp = []
        for j in range(0, N):
            tmp.append(ARR_MAX)
        visited.append(tmp)
    print(BFS(N, M, arr, visited))