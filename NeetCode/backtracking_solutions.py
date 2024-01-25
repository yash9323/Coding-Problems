# Neet Code BackTracking 

# 78 Subsets 
def subsets(nums):
    res = []
    def f(index,subset):
        if index == len(nums):
            print(subset)
            res.append(subset)
            return 
        f(index+1,subset)
        f(index+1,subset+[nums[index]])
    f(0,[])
    return res

# 39 Combination Sum 
def combinationSum(candidates, target):
    res = []
    def f(i,a):
        if i == len(candidates):
            return 
        if sum(a) == target:
            res.append(a)
            return 
        if sum(a) > target:
            return 
        f(i,a+[candidates[i]])
        f(i+1,a)
    f(0,[])
    return res

# 46 Permute 
def permute(nums):
    def f(n):
        res = []
        if len(n) == 1:
            return [n[:]]
        for i in range(len(n)):
            x = n.pop(0)
            rr = f(n)
            for r in rr:
                r.append(x)
            res.extend(rr)
            n.append(x)
        return res 
    return f(nums)

# 90 Subsets 2
def subsetsWithDup(nums):
    nums.sort()
    res = []
    def f(i,a):
        if i == len(nums):
            res.append(a)
            return 
        f(i+1,a + [nums[i]])
        while (i+1) < len(nums) and nums[i] == nums[i+1]:
            i += 1 
        f(i+1,a)
    f(0,[])
    return res

# 40 Combination Sum 2 
def combinationSum2(c, t):
    res = []
    c.sort()
    def f(i,a):
        if sum(a) == t:
            res.append(a[:])
            return 
        if sum(a) > t or i == len(c): return 
        f(i+1,a+[c[i]])
        while i + 1 < len(c) and c[i] == c[i+1]:
            i += 1
        f(i+1,a)
    f(0,[])
    return res

# 79 Word Search 
def exist(board, word):
    def f(i,j,k):
        if not 0 <= i < len(board) or not 0 <= j < len(board[0]): return False 
        if board[i][j] != word[k]: return False 
        if k == len(word) - 1: return True 
        d = [(1,0),(-1,0),(0,1),(0,-1)]
        for x,y in d:
            t = board[i][j]
            board[i][j] = -1 
            if f(i+x,j+y,k+1):
                return True 
            board[i][j] = t

    for r in range(len(board)):
        for c in range(len(board[0])):
            if f(r,c,0):
                return True 
    return False 

# 131 Palindrome Partitioning 
def partition(s):
    r = []
    def f(i,a):
        if i == len(s):
            r.append(a[:])
            return 
        for n in range(i,len(s)):
            x = s[i:n+1]
            if x == x[::-1]:
                a.append(x)
                f(n+1,a)
                a.pop()
    f(0,[])
    return r

# 17 Letter Combination of a Phone Number 
def letterCombinations(digits):
    if len(digits) == 0:
        return []
    m = {2:'abc',3:'def',4:'ghi',5:'jkl',6:'mno',7:'pqrs',8:'tuv',9:'wxyz'}
    r = []
    def f(i,s):
        if i == len(digits):
            r.append(s[:])
            return 
        for no in m[int(digits[i])]:
            f(i+1,s + no)
    f(0,"")
    return r

# 51 N-Queens
def solveNQueens(n):
    cols,d1,d2 = set(),set(),set()
    r = []
    board = [["." for _ in range(n)] for _ in range(n)]
    def f(r):
        if r == n:
            x = [''.join(l) for l in board]
            r.append(x)
            return 
        for c in range(n):
            if c in cols or (r+c) in d1 or (r-c) in d2:
                continue 
            cols.add(c)
            d1.add(r+c)
            d2.add(r-c)
            board[r][c] = "Q"
            f(r+1)
            cols.remove(c)
            d1.remove(r+c)
            d2.remove(r-c)
            board[r][c] = "."
    f(0)
    return r