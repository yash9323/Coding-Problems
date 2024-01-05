# Neet Code Stack 

#20 Valid Parentheses
def isValid(s):
    if len(s) % 2 != 0:
        return False 
    ob = ["(","[","{"]
    ss = []
    for b in s:
        if b in ob:
            ss.append(b)
        elif len(ss) > 0:
            if b == ")" and ss[-1] == "(":
                ss.pop()
            elif b == "}" and ss[-1] == "{":
                ss.pop()
            elif b == "]" and ss[-1] == "[":
                ss.pop()
            else:
                return False 
        else:
            return False
    if len(ss) > 0:
        return False 
    return True 

# 155 Min Stack 
class MinStack:
    # Maintain the min on every insertion 
    def __init__(self):
        self.stack = []
        self.mintracker = []
    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.mintracker:
            val = min(val,self.mintracker[-1])
        self.mintracker.append(val)
    def pop(self) -> None:
        self.stack.pop()
        self.mintracker.pop()
    def top(self) -> int:
        return self.stack[-1]
    def getMin(self) -> int:
        return self.mintracker[-1]

# 22 Generate Parenthesis 
def generateParenthesis(n):
    def h(n,s="",o=0,c=0,ouch=[]):
        if len(s) == 2*n:
            ouch.append(s)
            return 
        if o < n:
            h(n,s+"(",o+1,c,ouch)
        if c < o:
            h(n,s+")",o,c+1,ouch)
        return ouch
    return h(n)

# 150 Evaluate Reverse Polish Notation 
def evalRPN(tokens):
    stack = []
    for ch in tokens:
        if ch == "+":
            stack.append(stack.pop() + stack.pop())
        elif ch == "*":
            stack.append(stack.pop() * stack.pop())
        elif ch == "-":
            m,n = stack.pop(),stack.pop()
            stack.append(n-m)
        elif ch == "/":
            m,n = stack.pop(),stack.pop()
            stack.append(int(n/m))
        else:
            stack.append(int(ch))
    return stack[0]

# 739 Daily temperatures 
def dailyTemperatures(temperatures):
    res = [0] * len(temperatures)
    s = []
    for i,temp in enumerate(temperatures):
        while s and s[-1][0] < temp:
            a = s.pop()
            res[a[1]] = i - a[1]
        s.append([temp,i])
    return res

# 853 Car Fleet 
def carFleet(target, position, speed):
    carpairs = sorted([(p,s) for p,s in zip(position,speed)])[::-1]
    stack = []
    for p in carpairs:
        stack.append((target - p[0])/p[1])
        if len(stack) >=2 and stack[-1] <= stack[-2]:
            stack.pop()
    return len(stack)

# 84 Largest Historgram Rectangle 
def largestRectangleArea(heights):
    maxarea = 0 
    stack = []
    for i,h in enumerate(heights):
        s = i 
        while stack and stack[-1][1] > h:
            a = stack.pop()
            maxarea = max(maxarea, a[1] * (i-a[0]))
            s = a[0]
        stack.append((s,h))
    for i,h in stack:
        maxarea = max(maxarea, h * (len(heights)-i))
    return maxarea