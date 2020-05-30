import itertools

def solution(arr):
    answer = 999999999999
    group = list(range(len(arr)))
    tmp_group = list(itertools.combinations(group, int(len(arr) / 2)))

    for team1 in tmp_group:
        team2 = list(set(group) - set(team1))

        team1_cb = list(itertools.combinations(list(team1), 2))
        team2_cb = list(itertools.combinations(team2, 2))

        team1_val = 0
        team2_val = 0

        for i, j in team1_cb:
            team1_val += (arr[i][j] + arr[j][i])
        
        for i, j in team2_cb:
            team2_val += (arr[i][j] + arr[j][i])
                    
        if(answer > abs(team1_val - team2_val)):
            answer = abs(team1_val - team2_val)
    
    return answer

if __name__ == "__main__":

    N = input()
    w = []

    for i in range (0, int(N)):
        w.append(list(map(int, input().split())))
    
    print(solution(w))
