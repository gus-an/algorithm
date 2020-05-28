# 1759
# memory: 29380KB
# time: 76ms

mo = ['a', 'e', 'i', 'o', 'u']
answer = []
sortedAlpha = []

def isVaild(password):
  cnt = 0
  for m in mo:
    if m in password:
      cnt += 1
  
  if cnt > 0 and len(password) - cnt >= 2:
    return True
  else:
    return False

def DFS(L, idx, password):
  global answer
  if len(password) == L and isVaild(password):
    answer.append(password)
    return

  for i in range(idx, len(sortedAlpha)):
    DFS(L, i + 1, password + sortedAlpha[i])

if __name__ == "__main__":
  L, C = map(int, input().split())
  alpha = list(input().split())
  sortedAlpha = sorted(alpha)  
  DFS(L, 0, "")

  for password in answer:
    print(password)