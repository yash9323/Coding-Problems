# NeetCode  1DP 

# 70 Climbing Stairs 
def climbStairs(n):
    if n == 1 or n == 2: return n
    dp = [0 for _ in range(n+1)]
    dp[1],dp[2] = 1,2
    for i in range(3,n+1): dp[i] = dp[i-1]+dp[i-2]
    return dp[n]

# 746 Min Cost Climbing Stairs 
def minCostClimbingStairs(cost):
    dp = [0 for _ in range(len(cost))]
    dp[-1],dp[-2] = cost[-1],cost[-2]
    for i in range(len(cost)-3,-1,-1):
        dp[i] = cost[i] + min(dp[i+1],dp[i+2])
    return min(dp[0],dp[1])

# 198 House Robber 
def rob(nums):
    if len(nums) == 1: return nums[0]
    dp = [0 for _ in range(len(nums))]
    dp[-1],dp[-2] = nums[-1],max(nums[-1],nums[-2])
    for i in range(len(dp)-3,-1,-1): dp[i] = max(dp[i+1],dp[i+2]+nums[i])
    return max(dp[0],dp[1])

# 213 House Rober 2 
def rob(nn):
    if len(nn) < 3: return max(nn)
    def f(n):
        if len(n) == 1: return n[0]
        dp = [0 for _ in range(len(n))]
        dp[-1],dp[-2] = n[-1],max(n[-1],n[-2])
        for i in range(len(dp)-3,-1,-1): dp[i] = max(dp[i+1],dp[i+2]+n[i])
        return max(dp[0],dp[1])
    return max(f(nn[:-1]),f(nn[1:]))

# 647 Palindrome Substrings 
def countSubstrings(s):
    res = 0 
    def f(l,r):
        c = 0 
        while l >= 0 and r < len(s):
            if s[l] != s[r]: return c
            c += 1
            l -= 1
            r += 1
        return c
    for i in range(len(s)):
        res += f(i,i) + f(i,i+1)
    return res 

# 5 Longest Palindomic Substring 
def longestPalindrome(s):
    x = []
    def f(l,r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        x.append(s[l+1:r])
    for i in range(len(s)):
        f(i,i)
        f(i,i+1)
    return max(x,key=len)

# 322 Coin Change 
# Make the dp for Amount and the ways to make a amount == d store float inf since we want the minimum number of coins 
def coinChange(coins, a):
    dp = [float("inf") for _ in range(a+1)]
    dp[0] = 0 
    for i in range(1,a+1):
        for c in coins:
            if c <= i: dp[i] = min(dp[i],dp[i-c]+1)
    return -1 if dp[-1] == float("inf") else dp[-1]

# 152 Maximum Product Subarray 
# Maintianing a negative product for negatives to accomodate thoses negatives
def maxProduct(n):
    l = len(n)
    maxp = [n[0]] * l
    minp = [n[0]] * l
    for i in range(1,l):
        a = n[i]
        maxp[i] = max(a,a*maxp[i-1],a*minp[i-1])
        minp[i] = min(a,a*maxp[i-1],a*minp[i-1])
    return max(maxp)

# 139 Work Break
def wordBreak(s, wordDict):
    dp = [False for _ in range(len(s)+1)]
    dp[-1] = True 
    for i in range(len(s)-1,-1,-1):
        for w in wordDict:
            if (i + len(w)) <= len(s) and s[i:i+len(w)]==w:
                dp[i] = dp[i+len(w)] 
            if dp[i]: break
    return dp[0]

# 416 Partition Equal Subset Sum 
def canPartition(n):
    if sum(n) % 2 : 
        return False
    d,t = set(), sum(n) // 2
    d.add(0)
    for i in n:
        l = set()
        for v in d:
            l.add(v+i)
            l.add(v)
        d = l 
    if t in d:
        return True 
    else:
        return False
    
# 300 Longest Increasing Subsequence 
def lengthOfLIS(n):
    l = len(n)
    dp = [1 for _ in range(l)]
    for i in range(l-1,-1,-1):
        for j in range(i+1,l):
            if n[i] < n[j]: 
                dp[i] = max(dp[i],1+dp[j])
    return max(dp)

# 91 Decode Ways 
def numDecodings(s):
    if s[0] == "0":
        return 0 
    d = [0 for _ in range(len(s)+1)]
    d[0] = 1
    d[1] = 1
    for i in range(2,len(s)+1):
        if s[i-1] != '0':
            d[i] += d[i-1]
        t = int(s[i-2:i])
        if 10 <= t <= 26:
            d[i] += d[i-2]
    return d[-1]
