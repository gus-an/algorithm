from collections import deque

def solution(N, K):
    answer = "<"
    idx = 0

    q=deque()

    for i in range (0, N):
        q.appendleft(i + 1)

    while True:
        idx += 1

        for i in range (0, K - 1):
            q.appendleft(q.pop())

        answer += str(q.pop()) + ", "
        
        if (idx == N):
            answer = answer[0 : -2]
            answer += ">"
            break
    
    return answer

if __name__ == "__main__":
    N, K = map(int, input().split())

    print(solution(N, K))