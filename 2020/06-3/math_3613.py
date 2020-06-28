import sys

input = sys.stdin.readline

# f(x) = x^3
# f(x) = 0
def cube_root(num):
    answer = num
    i = 0

    while True:
        i += 1
        tmp = answer

        # f'(x) = 3 * x^2
        answer = answer - ((answer * answer * answer) - num) / (3 * (answer * answer))

        # print(tmp, answer)
        if (tmp - answer <= 0.0000000001):

            answer = '%.11f' % answer
            answer = str(answer)[:-1]
            break

    return answer

def solution(arr):
    answer = []

    for i in range (0, len(arr)):
        answer.append(cube_root(int(arr[i])))

    return answer

if __name__ == "__main__":

    N = input()
    arr = []
    for i in range (0, int(N)):
        arr.append(input())

    for i in range (0, len(solution(arr))):
        print(solution(arr)[i])