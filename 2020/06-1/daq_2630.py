import sys

input = sys.stdin.readline

def solution(arr, x_start, y_start, x_end, y_end, num): 
    global w_total, b_total

    if (num == 0):
        return 
    
    w_check = 0
    b_check = 0

    for i in range(x_start, x_end):
        for j in range(y_start, y_end):
            if (arr[i][j] == 0):
                w_check = w_check + 1
            else: 
                b_check = b_check + 1 
                
    total = num * num
    
    if (w_check == total):
        w_total = w_total + 1

    elif (b_check == total):
        b_total = b_total + 1

    else:
        x_mid = int((x_start + x_end) / 2)
        y_mid = int((y_start + y_end) / 2)

        num = int(num / 2)

        solution(arr, x_start, y_start, x_mid, y_mid, num)
        solution(arr, x_mid, y_start, x_end ,y_mid, num)
        solution(arr, x_start, y_mid, x_mid , y_end, num)
        solution(arr, x_mid, y_mid, x_end , y_end, num)


if __name__ == "__main__":
    w_total = 0
    b_total = 0

    N = input()

    arr = []
    for i in range (0, int(N)):
        arr.append(list(map(int, input().split())))

    solution(arr, 0, 0, int(N), int(N), int(N))
    print(w_total)
    print(b_total)