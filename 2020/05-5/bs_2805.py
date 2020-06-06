lst = []
pos = 0
diff = 2000000001

def cutTrees(pos, N):
    result = 0
    for i in range(0, N):
        if lst[i] > pos:
            result += lst[i] - pos
    return result

def BS(start, end, N, M):
    global pos
    global diff
    if start > end:
        return
    mid = (start + end) // 2
    bal = cutTrees(mid, N)

    if bal >= M and bal - M < diff and mid > pos:
        pos = mid
        diff = abs(M - bal)
    
    if bal >= M:
        return BS(mid + 1, end, N, M)
    elif bal < M:
        return BS(start, mid - 1, N, M)

if __name__ == "__main__": 
    N, M = map(int, input().split())
    tree = list(map(int, input().split()))
    lst = sorted(tree)
    BS(0, lst[N-1], N, M)
    print(pos)