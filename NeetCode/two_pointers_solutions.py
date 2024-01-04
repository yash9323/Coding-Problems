# Neet Code Two Pointers

# 125 Valid Palindrome 
def isPalindrome(s):
    l = ''.join([i.lower() for i in s if i.isalnum()])
    return l == l[::-1]

# 167 Sorted Two Sum 
def twoSum(numbers, target):
    i, j = 0, len(numbers) - 1
    while i < j:
        if numbers[i] + numbers[j] == target:
            return [i+1,j+1]
        if numbers[i] + numbers[j] < target:
            i += 1
        else:
            j -=1

# 15 3Sum 
def threeSum(nums):
    nums.sort()
    res = []
    for x in range(len(nums)):
        if nums[x] > 0 : 
            break   
        if x > 0 and nums[x] == nums[x-1]:
            continue 
        i,j = x+1, len(nums) - 1
        while i < j:  
            s = nums[x] + nums[i] + nums[j]
            if s == 0:
                res.append([nums[x],nums[i], nums[j]])
                i += 1 
                j -= 1 
                while nums[i] == nums[i-1] and i < j:
                    i+=1 
            elif s < 0:
                i += 1
            else:
                j -= 1
    return res

# 11 Container with most Water 
def maxArea(height):
    i,j = 0, len(height) - 1
    maxa = 0 
    while i < j :
        l = j - i 
        b = min(height[i],height[j])
        maxa = max(maxa,l*b)
        if height[i] < height[j]:
            i += 1
        else:
            j -= 1 
    return maxa 

# 42 Trapping Rain Water
def trap(height):
    def max_left_right(a):
        marray = []
        l = 0 
        for i in range(len(a)):
            marray.append(l)
            l = max(l,a[i])
        return marray
    rm = max_left_right(height)
    lm = max_left_right(height[::-1])[::-1]
    r = 0 
    for i in range(len(height)):
        t = min(rm[i],lm[i]) - height[i]
        if t > 0 :
            r += t
    return r 