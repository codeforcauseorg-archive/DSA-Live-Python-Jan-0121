# Recursion
def countSubsets(nums, s):
    return countSubsetsH(nums, s, 0)
def countSubsetsH(nums, s, index):
    if s == 0:
        return 1

    if index >= len(nums):
        return 0

    count = 0
    if nums[index] <= s:
        count += countSubsetsH(nums, s-nums[index], index+1)

    count += countSubsetsH(nums, s, index+1)

    return count

# DP
def countSubsetsDP(nums, s):
    dp = [[-1 for _ in range(s+1)] for _ in range(len(nums))]
    return countSubsetsDPH(nums, s, 0, dp)
def countSubsetsDPH(nums, s, index, dp):
    if s == 0:
        return 1

    if index >= len(nums):
        return 0

    if dp[index][s] != -1:
        return dp[index][s]

    count = 0
    if nums[index] <= s:
        count += countSubsetsDPH(nums, s-nums[index], index+1, dp)

    count += countSubsetsDPH(nums, s, index+1, dp)

    dp[index][s] = count
    return dp[index][s]

# Itr: Bottom Up
def countSubsetsItr(nums, s):
    dp = [[0 for _ in range(s+1)] for _ in range(len(nums))]

    for i in range(len(nums)):
        dp[i][0] = 1

    for i in range(1, s+1):
        dp[0][i] = 1 if nums[0] == i else 0

    for i in range(1, len(nums)):
        for j in range(1, s+1):
            dp[i][j] = dp[i-1][j]
            if nums[i] <= s:
                dp[i][j] += dp[i-1][j-nums[i]]

    return dp[len(nums)-1][s]


# Space optimized
def countSubsetsItrSpace(nums, s):
    dp = [0 for _ in range(s+1)]

    dp[0] = 1

    for i in range(1, s+1):
        dp[i] = 1 if nums[0] == i else 0

    for i in range(1, len(nums)):
        for j in range(s,,-1):
            if nums[i] <= s:
                dp[j] = dp[j] + dp[j-nums[i]]

    return dp[s]
