# Neet Code Math and Geometry 

# 202 Happy Number 
def isHappy(n):
    d = {}
    while True:
        s = 0 
        while n:
            s += ((n%10)**2)
            n //= 10 
        if s == 1:
            return True 
        if s in d:
            return False
        d[s] = 1
        n = s

# 73 Set Matrix Zeros 
def setZeroes(m):
    rr,cc = set(),set()
    for r in range(len(m)):
        for c in range(len(m[0])):
            if m[r][c] == 0:
                rr.add(r)
                cc.add(c)
    for r in rr:
        for c in range(len(m[0])):
            m[r][c] = 0 
    for r in range(len(m)):
        for c in cc:
            m[r][c] = 0 

# 66 Plus One 
def plusOne(d):
    for i in range(len(d)-1,-1,-1):
        if d[i] == 9: d[i] = 0 
        else:
            d[i] += 1
            return d
    return [1] + d

# 43 Multiply Strings 
def multiply(n, m):
    x,y = 0,0
    for i in n:
        x = x * 10 + (ord(i)-48)
    for i in m:
        y = y * 10 + (ord(i)-48)   
    return f'{x*y}' 

# 48 Rotate Image 
# reversing and swapping 
def rotate(m):
    m.reverse()
    a = len(m)
    for r in range(a):
        for c in range(r+1,a):
            m[r][c],m[c][r] = m[c][r],m[r][c]

# 2013 Detect Squares 
# Find Diagonal Point and then Edge Points Multiply the freq to get the total cout of squares
class DetectSquares:
    def __init__(self):
        self.m = {}
    def add(self, point):
        point = tuple(point)
        self.m[point] = 1 + self.m.get(point, 0)
    def count(self, point):
        r = 0 
        x, y = point
        for xx, yy in self.m: 
            if xx != x and abs(x-xx) == abs(y-yy): 
                r += self.m[xx, yy] * self.m.get((xx, y), 0) * self.m.get((x, yy), 0)
        return r 
    
# 50 Pow(x,n)
# Divide And Conquer
def myPow(x, n):
    def f(x,n):
        if x == 0: return 0 
        if n == 0: return 1 
        r = f(x,n//2)
        r = r * r 
        return r*x if n%2 else r 
    a = f(x,abs(n))
    return 1/a if n < 0 else a

# 54 Spiral Matrix 
def spiralOrder(m):
    res = []
    l,r = 0, len(m[0])
    t,b = 0, len(m)
    while l < r and t < b:
        for i in range(l,r):
            res.append(m[t][i])
        t += 1
        for i in range(t,b):
            res.append(m[i][r-1]) 
        r -= 1
        if not (l < r and t < b):
            break
        for i in range(r-1,l-1,-1):
            res.append(m[b-1][i])
        b -= 1
        for i in range(b-1,t-1,-1):
            res.append(m[i][l])
        l += 1
    return res   