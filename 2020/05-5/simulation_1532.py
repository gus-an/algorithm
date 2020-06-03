G = 0
S = 0
B = 0
count = 0

def mov1():
    global G, S, count
    G -= 1
    S += 9
    count += 1

def mov2():
    global G, S, count
    G += 1
    S -= 11
    count += 1

def mov3():
    global S, B, count
    S -= 1
    B += 9
    count += 1

def mov4():
    global S, B, count
    S += 1
    B -= 11
    count += 1


if __name__ == "__main__":
    G1, S1, B1 = map(int, input().split())
    G2, S2, B2 = map(int, input().split())
    
    G = G1 - G2
    S = S1 - S2
    B = B1 - B2

    while(True):
        # print(G, S, B, count)
        if (G >= 0 and S >= 0 and B >= 0):
            print(count)
            break
        elif (S < 0 and G >= 1):
            mov1()
        elif (S < 0 and B >= 11):
            mov4()        
        elif (G < 0 and S >= 11):
            mov2()
        elif (G < 0 and B >= 11):
            mov4()
        elif (B < 0 and S >= 1):
            mov3()
        elif (B < 0 and G >= 1):
            mov1()
        else:
            print(-1)
            break

