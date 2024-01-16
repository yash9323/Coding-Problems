# Neet Code Greedy 
import heapq

# 53 Maximum Subarray 
def maxSubArray(nums):
    c = 0 
    res = nums[0]
    for num in nums:
        if c < 0 :
            c = 0 
        c += num 
        res = max(res,c)
    return res 
    
# 55 Jump Game 
def canJump(nums):
    target = len(nums) - 1
    for i in range(len(nums)-1,-1,-1):
        canjump = i + nums[i]
        if canjump >= target:
            target = i 
    if target == 0:
        return True 
    else:
        return False 

# 45 Jump Game 2 
def jump(nums):
    steps, jumped, bestjump = 0,0,0
    for i in range(len(nums)-1):
        bestjump = max(bestjump,i + nums[i])
        if bestjump >= len(nums) - 1 :
            return steps + 1 
        if i == jumped :
            steps += 1 
            jumped = bestjump 
    return steps 

# 134 Gas Station 
def canCompleteCircuit(gas,cost):
    if sum(gas) < sum(cost):
        return -1 
    s = 0 
    t = 0 
    co = [gas[i] - cost[i] for i in range(len(gas))]
    for i,j in enumerate(co):
        t += j 
        if t < 0:
            t = 0 
            s = i + 1
    return s 

# 678 Valid Parenthesis String 
def checkValidString(s):
    i = j = 0
    for v in s:
        if v == "(":
            i += 1 
            j += 1 
        if v == ")":
            i -= 1 
            j -= 1
        if v == "*":
            i -= 1 
            j += 1
        if i < 0: i = 0 
        if j < 0: return False
    return i == 0

# 846 Hand of Straights 
def isNStraightHand(hand, groupSize):
    if len(hand) % groupSize != 0: return False
    m = {}
    h = list(set(hand)) 
    heapq.heapify(h)
    for n in hand:
        m[n] = m.get(n,0) + 1
    while h:
        a = h[0]
        for i in range(a,a+groupSize):
            if i not in m: return False
            m[i] -= 1
            if m[i] == 0:
                if h[0] == i: heapq.heappop(h)
                else: return False
    return True   

# 763 Partition Labels 
def partitionLabels(s):
    li = {}
    for i,v in enumerate(s): li[v] = i 
    res = []
    si = e = 0
    for i,v in enumerate(s):
        si += 1
        e = max(e,li[v])
        if e == i:
            res.append(si)
            si = 0 
    return res          

# 1899 Merge Triplets To Form Target Triplet
def mergeTriplets(triplets, target):
    r = set()
    for p in triplets:
        if all(p[i] <= target[i] for i in range(3)):
            for i in range(3):
                if p[i] == target[i]:
                    r.add(i)
    return len(r) == 3