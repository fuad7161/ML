def sqrt(x):
    l = 1
    r = 1e9
    ans = 0
    t = 100
    while(t > 0):
        t -= 1
        mid = (l+r)/2
        if mid**2 <= x:
            ans = mid
            l = mid
        else:
            r = mid
    return ans
