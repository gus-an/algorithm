from collections import deque

dh = [1, -1, 0, 0, 0, 0]
da = [0, 0, 0, 0, 1, -1]
db = [0, 0, 1, -1, 0, 0]

def BFS(L, R, C, building, visited, start):
    deq = deque()
    deq.append([start, 0])
    while len(deq):
        fnt = deq.popleft()
        for dir in range(0, 6):
            nh = fnt[0][0] + dh[dir]
            na = fnt[0][1] + da[dir]
            nb = fnt[0][2] + db[dir]
            if nh < 0 or nh >= L or na < 0 or na >= R or nb < 0 or nb >= C:
                continue
            if building[nh][na][nb] == 'E':
                return fnt[1] + 1
            if not visited[nh][na][nb] and building[nh][na][nb] == '.':
                visited[nh][na][nb] = True
                deq.append([[nh, na, nb], fnt[1] + 1])
    return 0                

if __name__ == "__main__":    
    while True:
        L, R, C = map(int, input().split())
        if L == 0 and R == 0 and C == 0:
            break
        building = []        
        visited = []
        start = []

        for i in range(0, L):
            ttmp = []
            for j in range(0, R):
                tmp = []
                for k in range(0, C):                    
                    tmp.append(False)
                ttmp.append(tmp)
            visited.append(ttmp)

        for i in range(0, L):
            tmp = []
            for j in range(0, R):
                ttmp = list(input())
                for k in range(0, len(ttmp)):
                    if ttmp[k] == 'S':
                        start = [i, j, k]
                tmp.append(ttmp)
            input()
            building.append(tmp)
        
        answer = BFS(L, R, C, building, visited, start)
        if answer:
            print("Escaped in " + str(answer) + " minute(s).")
        else:
            print("Trapped!")
        # print(building[0])
        # print(building[1])
        # print(building[2])
        # print(start)