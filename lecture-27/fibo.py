def fibo(n):
    if n < 2:
        return n
    return fibo(n-1) + fibo(n-2)

def fiboDP(n, dp):
    if n < 2:
        return n

    if dp[n]:
        return dp[n]

    dp[n] = fiboDP(n-1, dp) + fiboDP(n-2, dp)

    return dp[n]

print(fiboDP(40, [None for _ in range(41)]))
