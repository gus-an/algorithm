my_hash = {}

def rec(n):
    if n == 0:
        return 1
    else:
        a = 0
        for i in range(n):
            if i in my_hash:
                l = my_hash[i]
            else:
                l = rec(i)
                my_hash[i] = l
            if (n-1-i) in my_hash:
                r = my_hash[n-1-i]
            else:
                r = rec(n-1-i)
                my_hash[n-1-i] = r
            a += l * r
        return a

if __name__ == "__main__":
    N = int(input())

    result = rec(N)
    print(result)
    print(x)