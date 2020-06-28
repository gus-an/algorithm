from collections import deque

def bfs(M, N, tomato):
    first_tomato = []
    for i in range(N):
        for j in range(M):
            if lst[i][j] == 1:
                first_tomato.append((i, j))
    
    phase = 0
    dq = deque()
    dq.append(first_tomato)

    while dq:
        this_tomato = dq.popleft()
        next_tomato = []

        for (i, j) in this_tomato:
            # print(i, j)``
            if i-1 >= 0 and tomato[i-1][j] == 0:
                    tomato[i-1][j] = 1
                    next_tomato.append((i-1, j))
            if i+1 < N and tomato[i+1][j] == 0:
                    tomato[i+1][j] = 1
                    next_tomato.append((i+1, j))
            if j-1 >= 0 and tomato[i][j-1] == 0:
                    tomato[i][j-1] = 1
                    next_tomato.append((i, j-1))
            if j+1 < M and tomato[i][j+1] == 0:
                    tomato[i][j+1] = 1
                    next_tomato.append((i, j+1))

        if not next_tomato:
            if has_zero(tomato):
                phase = -1

            return phase
        else:
            dq.append(next_tomato)
            phase += 1

        # pretty(tomato)
    
def pretty(lst):
    for row in lst: 
        for val in row:
            print('{:3}'.format(val), end='')
        print()

def has_zero(lst):
    for row in lst:
        for val in row:
            if val == 0:
                return True
    return False

if __name__ == "__main__":
    M, N = map(int, input().split())
    lst = []
    for i in range(0, N):
        lst.append(list(map(int, input().split())))

    # M, N = 6, 4

    # print(M, N)

    # lst = [[0, -1, 0, 0, 0, 0],
    #        [-1, 0, 0, 0, 0, 0],
    #        [0, 0, 0, 0, 0, 0],
    #        [0, 0, 0, 0, 0, 1]]


    print(bfs(M, N, lst))