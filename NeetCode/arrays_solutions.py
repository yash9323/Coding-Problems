# Neet Code Array & Hashing 

# 217 Contains Duplicates 
def containsDuplicates(nums):
    hashmap = {}
    for num in nums:
        if num in hashmap:
            return True 
        hashmap[num] = 1 
    return False 

# 242 Valid Anagram 
def isAnagram(s,t):
    if sorted(list(s)) == sorted(list(t)):
        return True 
    else: 
        return False 
    
# 1 Two Sum 
def twoSum(nums,target):
    hashmap = {}
    for index in range(len(nums)):
        if nums[index] not in hashmap:
            hashmap[target-nums[index]] = index 
        else:
            return [hashmap[nums[index]],index]
        
# 49 Group Anangrams 
def groupAnagrams(strs):
    hashmap = {}
    for string in strs:
        s = ''.join(sorted(list(string)))
        if s in hashmap:
            hashmap[s].append(string)
        else:
            hashmap[s] = [string]
    return list(hashmap.values())

# 347 Top K Frequent Elements 
def topKFrequent(nums,k):
    hashmap = {}
    for num in nums:
        hashmap[num] = hashmap.get(num,0) + 1 
    return list(dict(sorted(hashmap.items(), key= lambda item: item[1],reverse=True)).keys())[:k]

# 238 Product of Array Except Self 
def productExceptSelf(nums):
    res = [1 for _ in range(len(nums))]
    ssum, psum = 1,1
    for index in range(len(nums)):
        res[index] *= psum 
        res[-1-index] *= ssum 
        psum *= nums[index]
        ssum *= nums[-1-index]
    return res 

# 36 Valid Sudoku 
def isValidSudoku(board):
        rowmap = {k:[] for k in range(len(board))}
        columnmap = {k:[] for k in range(len(board[0]))}
        sectormap = {(row//3,col//3):[] for col in range(len(board[0])) for row in range(len(board))}

        for row in range(len(board)):
            for col in range(len(board[0])):
                q = board[row][col]
                if q == ".":
                    continue 
                if q in rowmap[row] or q in columnmap[col] or q in sectormap[(row//3,col//3)]:
                    return False
                else:
                    rowmap[row].append(q)
                    columnmap[col].append(q)
                    sectormap[(row//3,col//3)].append(q)
        return True 

# 128 Longest Consecutive Sequence 
def longestConsecutive(nums):
        nums = set(nums)
        count = 0 
        while count < len(nums):
            n = nums.pop()
            uppercount = n + 1
            while uppercount in nums:
                nums.remove(uppercount)
                uppercount += 1
            lowercount = n - 1
            while lowercount in nums:
                nums.remove(lowercount)
                lowercount -= 1
            count = max(count,uppercount-lowercount-1)
        return count

# 659 Encode Decode Strings 
def encode(strs):
    return '$%#@!'.join(strs)

def decode(str):
    return str.split('$%#@!')