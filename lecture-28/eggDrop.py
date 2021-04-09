import math

def eggDrop(egg, floor):
    if floor == 0:
        return 0

    if egg == 1:
        return floor

    ans = math.inf

    for i in range(1, floor+1):
        sol = max(eggDrop(egg-1, i-1), eggDrop(egg, floor-i)) + 1;
        ans = min(ans, sol)

    return ans


# DP
def eggDrop(egg, floor, dp):
    if floor == 0:
        return 0

    if egg == 1:
        return floor

    if dp[egg][floor]:
        return dp[egg][floor]

    ans = math.inf

    for i in range(1, floor+1):
        sol = max(eggDrop(egg-1, i-1, dp), eggDrop(egg, floor-i, dp)) + 1;
        ans = min(ans, sol)

    dp[egg][floor] = ans
    return ans

# ITR
def eggDropItr(eggs, floors):
    dp = [[0 for _ in range(floors+1)] for _ in range(eggs+1)]

    for i in range(eggs+1):
        dp[i][0] = 0
    for i in range(floors+1):
        dp[1][i] = i

    for e in range(1, eggs+1):
        for f in range(0, floors+1):
            ans = math.inf
            for i in range(1, f+1):
                sol = max(dp[e-1][i-1], dp[e-1][f-i]) + 1;
                ans = min(ans, sol)

            dp[e][f] = ans

    return dp[eggs][floors]
