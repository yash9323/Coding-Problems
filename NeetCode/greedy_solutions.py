# Neet Code Greedy 

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

