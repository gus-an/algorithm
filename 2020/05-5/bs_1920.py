lst = []

def BS(start, end, target):
    if start > end:
        return 0
    mid = (start + end) // 2
    if lst[mid] == target:
        return 1
    elif lst[mid] < target:
        return BS(mid + 1, end, target)
    else:
        return BS(start, mid - 1, target)

if __name__ == "__main__":
    N = int(input())
    numList = list(map(int, input().split()))
    M = int(input())
    searchList = list(map(int, input().split()))

    lst = sorted(numList)
    for num in searchList:
        print(BS(0, len(lst) - 1, num))