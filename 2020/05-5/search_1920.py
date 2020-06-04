def binary_search (arr, target):

    if len(arr) == 1:
        if arr[0] == target:
            return 1
        else:
            return 0

    if len(arr) == 0:
        return 0
        
    med = len(arr) // 2

    if target == arr[med]:
        return 1
    elif target > arr[med]:
        return binary_search(arr[med:], target)
    else:
        return binary_search(arr[:med], target)

def solution(input_arr, target_arr):
    input_arr = sorted(input_arr)

    for i in range (0, len(target_arr)):
        print(binary_search(input_arr, target_arr[i]))

if __name__ == "__main__":

    N = int(input())
    n_arr = list(map(int, input().split()))
    
    M = int(input())
    x_arr = list(map(int, input().split()))

    solution(n_arr, x_arr)
