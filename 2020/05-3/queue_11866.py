if __name__ == "__main__":
    N, J = map(int, input().split())
    a = list(range(1, N+1))
    b = []

    alen = len(a)
    i = J
    while alen >= J: 
        pop = 0
        while i <= alen:
            b.append(a.pop(i - 1 - pop))
            i += J
            pop += 1
        i = i - alen
        alen = len(a)

    while alen > 0:
        # print('a', a, 'b', b, 'alen', alen, 'i', i)
        while i > alen:
            i = i - alen
        # print(i)
        b.append(a.pop(i - 1))
        i += J - alen
        alen = len(a)

    sol = "<"
    for idx, val in enumerate(b):
        if idx + 1 == len(b):
            sol = sol + str(val) + '>'
        else:
            sol = sol + str(val) + ', '
    
    print(sol)