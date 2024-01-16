# Leet Code Problem 13 Roman to Integer
def romanToInt(s):
    chart = {
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000
        }
    result = 0
    for i in range(len(s)):
        if i > 0 and chart[s[i]] > chart[s[i - 1]]:
            result += chart[s[i]] - 2 * chart[s[i - 1]]
        else:
            result += chart[s[i]]
        print(result)
    return result
    
# Leet Code Problem 141 Linked List Cycle
def hasCycle(head):
    slow = head 
    fast = head 
    while fast and fast.next:
        slow = slow.next 
        fast = fast.next.next 
        if slow == fast:
            return True 
    else:
        return False 
    
# Leet Code Problem 2965 Find Missing and Repeated Values
def findMissingAndRepeatedValues(grid):
    c = {}
    a = b = None
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            c[grid[row][col]] = c.get(grid[row][col],0) + 1
    for i in range(1,len(grid)*len(grid[0])+1):
        if i in c and c[i] == 2:
            a = i 
        elif i not in c:
            b = i 
        if a and b:
            return [a,b]

# Leet Code Problem 190 Reverse Bits
def reverseBits(n):
    binary = bin(n)[2:].zfill(32)
    return int(binary[::-1], 2)

# Leet Code Problem 108 Convert Sorted Array to Binary Search Tree
def sortedArrayToBST(nums):
    def lol(nums):
        if not nums:
            return None 
        mid = len(nums)//2
        node = TreeNode(nums[mid])
        node.left = lol(nums[:mid])
        node.right = lol(nums[mid+1:])
        return node 
    return lol(nums)

# Leet Code Problem 101 Symmetric Tree
def isSymmetric(root):
    def checkmirror(left,right):
        if not left and not right:
            return True 
        if not left or not right or left.val != right.val:
            return False
        return checkmirror(left.left,right.right) and checkmirror(left.right,right.left)
    if root is None:
        return True 
    return checkmirror(root.left,root.right)

# Leet Code Problem 160 Intersection of Two Linked Lists
def getIntersectionNode(headA, headB):
    def length(head):
        curr = head 
        lenn = 0 
        while curr:
            lenn+=1 
            curr = curr.next 
        return lenn
    lena = length(headA)
    lenb = length(headB)
    heada = headA
    headb = headB
    if lena < lenb:
        for i in range(lenb-lena):
            headb = headb.next 
    else:
        for i in range(lena-lenb):
            heada = heada.next 
    
    while heada and headb:
        if heada == headb:
            return heada 
        else:
            heada = heada.next 
            headb = headb.next 
    return None 

# Leet Code Problem 21 Merge Two Sorted Lists
def mergeTwoLists(list1, list2) :
    i = list1
    j = list2
    l = []
    while i and j :
        if i.val <= j.val:
            l.append(i.val)
            i = i.next 
        else:
            l.append(j.val)
            j = j.next
    while i:
        l.append(i.val)
        i = i.next
    while j:
        l.append(j.val)
        j = j.next
    if l:
        out = ListNode(l[0])
        nextt = out
    else:
        return i
    for i in l[1:]:
        nextt.next = ListNode(i)
        nextt = nextt.next
    return out 

# Leet Code Problem 234 Palindrome Linked List
def isPalindrome(head):
    s = ""
    curr = head
    while curr:
        s += str(curr.val)
        if curr.next:
            curr = curr.next
        else:
            break
    if s == s[::-1]:
        return True 
    else:
        return False

# Leet Code Problem 14 Longest Common Prefix
def longestCommonPrefix(strs):
        if not strs:
            return ""
        shortest_str = min(strs,key=len)
        for i,ch in enumerate(shortest_str):
            for other_strings in strs:
                if other_strings[i] != ch:
                    return shortest_str[:i]
        return shortest_str

# Leet Code Problem Hamming Weight 
def hammingWeight(n) :
    ans = 0
    while n:
        n = n & (n-1)
        ans += 1
    return ans 

# Leet Code Problem 350 Intersection of Two Arrays II
def intersection_of_two_arrays(nums1,nums2):
    if len(nums1) < len(nums2):
        return intersection_of_two_arrays(nums2,nums1)
    map1 = {}
    result = []
    for i in nums1:
        if i not in map1:
            map1[i] = 1
        else:
            map1[i] += 1
    for i in nums2:
        try:
            if map1[i] > 0:
                result.append(i)
                map1[i]-=1
        except :
            pass
    return result

# If sorted we can use merge sort process to get the common 
# if nums1 less than nums2 and sorted time is O(nums1)

# Leet Code Problem 121 Best Time to Buy and Sell Stock
def best_buy_sell(prices):
    profit = 0
    minb = 999999999999
    for i in range(len(prices)):
        if minb>prices[i]:
            minb = prices[i]
        profit = max(profit,prices[i]-minb)
    return profit
best_buy_sell([7,6,5,20,18,97,65])

# Leet Code Problem 326 Power of Three
def power_of_three(n):
    if n == 0:
        return False 
    else :
        observed = [n]
        while observed[-1] != 1 :
            if n % 3 > 0 :
                return False
            else :
                n = n//3
                observed.append(n)
        return True
power_of_three(243)
        
# Leet Code Problem 283 Move Zeroes
def moveZeros(nums):
    for i in range(len(nums)):
        if nums[i] == 0:
            for j in range(i,len(nums)):
                if nums[j] != 0:
                    nums[i],nums[j] = nums[j],nums[i]
                    break
    return nums
moveZeros([1,0,0,3,4,6,0,0])

# Leet Code Problem 171 Excel Sheet Coloumn Number 
def titleToNumber(columnTitle):
    ans = 0 
    power = 0 
    for i in reversed(columnTitle):
        no = ord(i)-64
        ans += no * 26**power
        power += 1
    return ans

titleToNumber("ABC")

# Leet Code Problem 94 Binary Tree Inorder Traversal
def inorderTraversal(root):
    ans = []
    def inn(root):
        if root is None :
            return 
        if root.left:
            inn(root.left)
        ans.append(root.val)
        if root.right:
            inn(root.right)
    inn(root)
    return ans

# Leet Code Problem 104 Maximum Depth of Binary Tree
def max_depth_binary_tree(root):
    if root is None:
        return 0 
    return max(1+max_depth_binary_tree(root.right),1+max_depth_binary_tree(root.left))

# Leet Code Problem 20 Valid Parentheses
def valid_parentheses(s):
    ss = []
    for i in s:
        if (i == "(" or i =="[" or i == "{"):
            ss.append(i)
        if len(ss) == 0:
            return False
        if i == ")" and ss.pop() !="(":
            return False
        if i == "}" and ss.pop() !="{":
            return False
        if i == "]" and ss.pop() !="[":
            return False
    if len(ss) == 0 :
        return True
    else: 
        return False
valid_parentheses("(){}[]")    

# Leet Code Problem 88 Merge Sorted Array 
def merge_sorted_array(nums1,nums2,m,n):
    j=0
    for i in range(m,len(nums1)):
        nums1[i] = nums2[j]
        j+=1 
    nums1.sort()
    return nums1
nums1 = [1,2,3,0,0,0] 
nums2 = [2,5,6]
m = 3 
n = 3
merge_sorted_array(nums1,nums2,m,n)

# Leet Code Problem 412 Fizz Buzz  
n = 5
def fizzbuzz(n):
    out = []
    for i in range(1,n+1):
        if i % 3 == 0 and i % 5 ==0 :
            out.append("FizzBuzz")
        else:
            if i % 3 == 0 :
                out.append("Fizz")
            elif i % 5 == 0 :
                out.append("Buzz") 
            else:
                out.append(str(i))
    return out
fizzbuzz(10)

# Leet Code Problem 387  First Unique Character in a String
def firstUniqueChar(s):
    d = {}
    for i in s:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1 
    for i in d:
        if d[i] == 1:
            return s.index(i)
    else:
        return -1
firstUniqueChar("yashbhutoria")

# Leet Code Problem 268 Missing Number
def missingNumber(nums):
    actual_sum = sum(nums)
    dd = [i for i in range(0,len(nums)+1)]
    total_sum = sum(dd)
    print(total_sum)
    print(actual_sum)
    return total_sum - actual_sum
missingNumber([3,0,1])

# Leet Code Problem 118 Pascals Triangle
def pascal_triangle(numRows):
    ans = [[1]]
    if numRows == 1 :
        return ans 
    ans.append([1,1])
    if numRows == 2 :
        return ans 
    for _ in range(numRows-2):
        s = []
        s.append(1)
        last_aay = ans[-1]
        pointer1 = 0
        pointer2 = 1
        for _ in range(0,len(last_aay)-1):
            sol = last_aay[pointer1] + last_aay[pointer2]
            pointer1+=1
            pointer2+=1
            s.append(sol)
        s.append(1)
        ans.append(s)
    return ans
pascal_triangle(7)

# Leet Code Problem 206 Reverse Link List 
def reverse_link_list(head):
    current = head
    prev = None 
    while current :
        nextnode = current.next
        current.next = prev
        prev = current 
        if nextnode is None:
            head = current 
        current = nextnode
    return head

# Leet Code Problem 125 Valid String Palindrome 
def valid_palindrome(s):
    d=""
    for i in s:
        if i.isalnum():
            d+=i.lower()
    if d == d[::-1]:
        return True
    else:
        return False
valid_palindrome('Yash Hsay')

# Leet Code Problem 66 Plus One 
def plus_one(digits):
    no = ""
    out = []
    for i in digits:
        no+=str(i)
    no = int(no)
    no += 1
    no = str(no)
    for i in no:
        out.append(int(i))
    return out
plus_one([9])

# Leet Code Problem 69 Sqrt(x)
def sqrt(x):
    d ={
        0:0,
        1:1,
        2:1
    }
    if x in d:
        return d[x]
    for i in range(2,x):    
        a = i*i
        if a == x:
            return i  
        if a > x:
            return i-1
sqrt(8)               
# Can Also be done with binary search 
 
# Leet Code Problem 26 Remove Duplicates from Sorted Array
def remove_duplicates(array):
    a = sorted(list(set(array)))
    for i in range(len(a)):
        array[i] = a[i]
    return len(a)
remove_duplicates([-1,0,0,0,0,3,3])

# Leet Code Problem 202 Happy Number
def happy_number(n):
    old_sums = []
    while True:
        no = str(n)
        summ = 0 
        for i in no:
            summ +=int(i)**2
        if summ == 1:
            return True
        if summ in old_sums:
            return False
        old_sums.append(summ)
        n = summ
happy_number(19)

# Leet Code Problem 169 Majority Element
def majority_element(nums):
    if len(nums) == 1 :
        return 1
    cond = len(nums) // 2
    m2 = {}
    for i in nums:
        if i not in m2:
            m2[i] = 1 
        else:
            m2[i] += 1 
            if m2[i] > cond:
                return i 
majority_element([3,2,3,2,2,2,2,2,5])

# Leet Code Problem 344 Reverse String
def reverse_string(s):
    for i in range(len(s)//2):
        s[i],s[-1-i] = s[-1-i],s[i]
    return s 
reverse_string(['e', 'd', 'c', 'b', 'a'])

# Leet Code Problem 217 Contains Duplicate
def contains_duplicates(nums):
    m1 = {}
    for i in nums:
        if i not in m1:
            m1[i] = 1
        else:
            m1[i] += 1
            return True
    return False

nums = [1,2,3]
contains_duplicates(nums)

# Leet Code Problem 242 => Valid Anagram
def valid_anagram(s,t):
    if len(s) != len(t):
        return False
    d = {}
    for i in s:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    for j in t:
        if j in d:
            d[j] -= 1
            if d[j] == 0 :
                del d[j]
        else:
            return False
    return True 
valid_anagram('yash','hsay')
