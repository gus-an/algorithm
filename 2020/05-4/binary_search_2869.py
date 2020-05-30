import math

def snail(A, B, V) :
    delta = A - B
    lo = 0
    hi = math.ceil(V / delta) # 날짜의 상한선

    while(lo < hi):
        # 검색 날짜
        # 올림은 lo 랑 mid 가 같아지지 않기 위함
        mid = math.ceil((hi + lo) / 2)

        night = mid * (delta) # 밤의 위치
        day = night + B # 낮의 위치

        # print('lo', lo, 'hi', hi, 'mid', mid, 'day', day, 'night', night)

        if day < V: # 낮에도 도달 못함
            lo = mid
        elif day - delta >= V: # 전날 밤에도 도달
            hi = mid
        else:
            return mid

if __name__ == "__main__":
    A, B, V = map(int, input().split())
    print(snail(A, B, V))
