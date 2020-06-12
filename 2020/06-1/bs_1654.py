import sys

lanLst = []
maxLen = 0

def countLan(len):
    result = 0
    for lan in lanLst:
        result += lan // len 
    return result

def BS(start, end, target):
    global maxLen
    if start > end:
        return 
    mid = (start + end) // 2
    tmpCount = countLan(mid)
    if tmpCount < target:
        return BS(start, mid - 1, target)
    elif tmpCount >= target:
        if mid > maxLen:
            maxLen = mid
        return BS(mid + 1, end, target)


if __name__ == "__main__":
    N, M = map(int, input().split())    
    for i in range(0, N):
        lanLst.append(int(input()))
    # N, M = 4, 11
    # lanLst = [802, 743, 457, 539]

    BS(0, sys.maxsize, M)
    print(maxLen)