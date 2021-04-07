def partitionSubset(arr):
    s = sum(arr)

    if s%2 != 0:
        return False
    return partitionSubsetH(arr, s//2, 0)

def partitionSubsetH(arr, s, index):
    if s == 0:
        return True

    if len(arr) == 0 or index >= len(arr):
        return False

    if arr[index] <= s:
        if partitionSubsetH(arr, s-arr[index], index+1):
            return True
    return partitionSubsetH(arr, s, index+1):


# Top Down DP
def partitionSubset(arr):
    s = sum(arr)

    if s%2 != 0:
        return False

    dp = [[None for _ in range(s//2 + 1)] for _ in range(len(arr))]
    return partitionSubsetH(arr, s//2, 0, dp)

def partitionSubsetH(arr, s, index):
    if s == 0:
        return True

    if len(arr) == 0 or index >= len(arr):
        return False

    if dp[index][s] == None:
        if arr[index] <= s:
            if partitionSubsetH(arr, s-arr[index], index+1, dp):
                dp[index][s] = True
                return True

    dp[index][s] = partitionSubsetH(arr, s, index+1, dp):

    return dp[index][s]

def itr(nums):
    s = sum(nums)
    if s % 2 != 0:
        return False

    s = s // 2
    n = len(nums)

    dp = [[False for _ in range(s+1)] for _ in range(n)]

    for i in range(n):
        dp[i][0] = True
    for j in range(1, s+1):
        dp[0][j] = nums[0] == j

    for i in range(1, n):
        for j in range(1, s+1):

            if dp[i-1][j]:
                dp[i][j] = True
            elif j >= nums[i]:
                dp[i][j] = dp[i-1][j-nums[i]]

    return dp[n-1][s]
