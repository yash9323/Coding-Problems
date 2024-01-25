# Neet Code Sliding Window 

# 121 Best Time to Buy and Sell Stock 
def maxProfit(prices):
    smallest_price = float("infinity")
    profit = 0 
    for price in prices:
        profit = max(profit,price - smallest_price)
        smallest_price = min(smallest_price,  price)
    return profit

# 3 Longest Substring Without Repeating Characters 
def lengthOfLongestSubstring(s):
    d = {}
    l,r = 0,0 
    res = 0 
    while r < len(s):
        if s[r] in d:
            l = max(l,d[s[r]]+1)
        res = max(res,r-l+1)
        d[s[r]] = r 
        r += 1
    return res 

# 424 Longest Repeating Character Replacement 
def characterReplacement(s, k):
    d = {}
    l = 0 
    mm = 0 
    res = 0 
    for r,ch in enumerate(s):
        d[ch] = d.get(ch,0) + 1
        mm = max(mm,d[ch])
        if (r-l+1) - mm > k:
            d[s[l]] -= 1
            l += 1
        res = max(res,r-l+1)
    return res

# 567 Permutation in a String 
def checkInclusion(s1, s2):
    if len(s1) > len(s2): return False 
    d,w = {}, {}
    for i in s1: d[i] = d.get(i,0) + 1
    for i in range(len(s1)): w[s2[i]] = w.get(s2[i],0) + 1
    if d == w: return True 
    for i in range(len(s1),len(s2)):
        w[s2[i]] = w.get(s2[i],0) + 1
        if w[s2[i-len(s1)]] == 1: del w[s2[i-len(s1)]]
        else: w[s2[i-len(s1)]] -= 1
        if d == w: return True 
    return False

