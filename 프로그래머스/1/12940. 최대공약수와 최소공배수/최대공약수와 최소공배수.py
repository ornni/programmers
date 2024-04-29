def MOD(a, b):
    x = max(a, b)
    y = min(a, b)
    if b == 0:
        return a
    else:
        return MOD(b, a%b)
    
def solution(n, m):
    gcd = MOD(n, m)
    lcm = n * m / gcd
    answer = [gcd, lcm]
    return answer