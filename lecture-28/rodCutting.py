def rodCutting(arr, n):
    if n == 0:
        return 0

    profit = 0

    for i in range(0, n):
        profit = max(profit, arr[i] + rodCutting(arr, n-i-1))

    return profit


def rcDP(arr, n):
    dp = [None for _ in range(n+1)]
    return rodCuttingDP(arr, n, dp)
def rodCuttingDP(arr, n, dp):
    if n == 0:
        return 0

    if dp[n]:
        return dp[n]

    profit = 0

    for i in range(0, n):
        profit = max(profit, arr[i] + rodCuttingDP(arr, n-i-1, dp))

    dp[n] = profit
    return dp[n]

def rcItr(arr, n):
    dp = [0 for _ in range(n+1)]

    dp[0] = 0

    for i in range(1, n+1):
        profit = 0

        for j in range(0, i):
            profit = max(profit, arr[j] + dp[i-j-1])

        dp[i] = profit

    return dp[n]
