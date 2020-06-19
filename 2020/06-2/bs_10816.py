# bs_10816
# 메모리: 112972KB, 시간: 4396ms

from collections import Counter

cards = []
lst = []
dic = {}

def BS(start, end, num):
    if start > end:
        return 0
    mid = (start + end) // 2

    if cards[mid] == num:
        return dic[cards[mid]]
    elif cards[mid] < num:
        return BS(mid + 1, end, num)
    elif cards[mid] > num:
        return BS(start, mid - 1, num)

if __name__=="__main__":
    N = int(input())
    cards = list(map(int, input().split()))
    M = int(input())
    lst = list(map(int, input().split()))

    dic = Counter(cards)
    cards = sorted(cards)

    for idx, num in enumerate(lst):
        print(BS(0, len(cards) - 1, num), end=" ")