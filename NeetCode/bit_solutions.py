# NeetCode Bit Manipulation 

# 136 Single Number 
def singleNumber(nums):
    # use xor to cancel out two same numbers 
    out = 0 
    for no in nums:
        out ^= no 
    return out 

# 191 Number of 1 Bits 
def hammingWeight(n):
    r = 0 
    while n:
        r += n & 1
        n = n >> 1
    return r

# 338 Counting Bits 
def countBits(n):
    o = []
    for i in range(n+1):
        o.append(i.bit_count())
    return o

# 190 Reverse Bits
# n & 1 and left shift the reversed things 
def reverseBits(n):
    r = 0 
    for i in range(32):
        r = (r << 1) | (n&1)
        n >>= 1
    return r

# 268 Missing Number 
def missingNumber(nums):
    r = 0 
    for i in range(1,len(nums)+1):
        r ^= i 
        r ^= nums[i-1]
    return r

# 7 Reverse Integer 
# Reverse the Integer using the standard process and then check the bounds return negative or postive wrt to x
def reverse(x):
    a,b = (-2**31) , (2**31+1)
    def f(x):
        r = 0 
        while x:
            r = (r*10) + (x%10)
            x //= 10 
        return r 
    r = f(abs(x))
    if r < a or r > b: return 0 
    if x < 0: return -r
    return r

# 371 Sum of Two Integers 
# mask to check the int size and perfom xor for res and carry is ans returning ans for positive and negative 
def getSum(a, b):
    m = 0xFFFFFFFF
    while (b & m) > 0:
        t = (a&b) << 1
        a ^= b
        b = t
    return a&m if b > 0 else a