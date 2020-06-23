# bs_2512
# 메모리: 29588KB,시간: 72ms

reqs = []
maxSum = 0

def calSum(mid):
  result = 0
  for req in reqs:
    if mid >= req:
      result += req
    else:
      result += mid
  return result

def BS(start, end, M):
  global maxSum   
  if start > end:
    return
  
  mid = (start + end) // 2
  tmpSum = calSum(mid)

  if tmpSum == M:
    maxSum = mid
    return 
  elif tmpSum < M:
    if mid > maxSum:
      maxSum = mid
    return BS(mid + 1, end, M)
  elif tmpSum > M:
    return BS(start, mid - 1, M)

if __name__ == "__main__":
  N = int(input())
  reqs = list(map(int, input().split()))
  M = int(input())
  BS(0, max(reqs), M)
  print(maxSum)