import sys

input = sys.stdin.readline

def solution(inp):
    answer = ""
    flag1 = False
    flag2 = False
    i = -1

    while True:
        i += 1
        if (inp[0].isupper()):
            answer = "Error!"
            break
        elif (inp[len(inp)-2] == "_"):
            answer = "Error!"
            break
        
        if (len(inp) <= i):
            if (flag1 and flag2):
                answer = "Error!"
            break
        if (inp[i].isupper()):
            answer += "_" + inp[i].lower()
            flag1 = True
        elif (inp[i] == "_"):
            if (inp[i + 1].isupper()):
                answer = "Error!"
                break
            elif (inp[i + 1] == "_"):
                answer = "Error!"
                break
            else:
                answer += inp[i + 1].upper()
                inp = answer + inp[i + 2:]
                flag2 = True
        else:
            answer += inp[i]
        
    return answer

if __name__ == "__main__":

    N = input()

    print(solution(N))
