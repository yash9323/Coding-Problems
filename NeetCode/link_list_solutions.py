# Link List Neet Code 

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
# 206 Reverse a Link List 
def reverseList(head):
    p = None
    c = head
    while c:
        n = c.next
        c.next = p
        p = c
        if n == None:
            head = c
            return head 
        c = n

# 21 Merge Two Sorted Lists 
def mergeTwoLists(list1, list2):
    x = list1 
    y = list2 
    if x and y:
        if x.val <= y.val:
            r = x
            p1 = x.next 
            p2 = y
        else:
            r = y
            p1 = x
            p2 = y.next
    else:
        return x if x else y 
    ans = r
    while p1 and p2:
        if p1.val < p2.val:
            r.next = p1
            p1 = p1.next
        else:
            r.next = p2
            p2 = p2.next
        r = r.next
    if p1:
        r.next = p1 
    else:
        r.next = p2
    return ans 

# 143 Reorder Link List 
def reorderList(head):
    s, f = head,head
    while f and f.next:
        s = s.next 
        f = f.next.next 
    p = None
    while s:
        n = s.next 
        s.next = p 
        p = s
        s = n
    l,r = head,p
    while r.next:
        t = l.next 
        tt = r.next 
        l.next = r
        r.next = t
        l = t
        r = tt
    return head

# 19 Remove Nth Node from the End of List 
def removeNthFromEnd(head, n):
    current = head
    count = 0 
    while current:
        count += 1
        current = current.next
    if count == 1:
        return None
    to_remove = count - n
    if to_remove == 0:
        head = head.next 
        return head
    index = 0 
    current = head
    prev = None 
    while current:
        if index == to_remove:
            prev.next = current.next 
            break
        else:
            prev = current
            current = current.next
            index += 1
    return head

# 141 Link List Cycle 
def hasCycle(head):
    s, f = head, head 
    while f and f.next:
        s = s.next 
        f = f.next.next
        if s == f:
            return True 
    return False

# 287 Find the Duplicate Number 
def findDuplicate(nums):
    s = f = nums[0]
    while True:
        s = nums[s]
        f = nums[nums[f]]
        if s == f:
            break
    s = nums[0]
    while s != f:
        s = nums[s]
        f = nums[f]
    return s

# 138 Copy List with Random Pointer 
def copyRandomList(head):
    d = {}
    def f(h):
        if h == None: return None
        if h in d: return d[h]
        n = Node(h.val,h.next)
        d[h] = n
        n.next = f(h.next)
        n.random = f(h.random)
        return n
    return f(head)

# 2 Add Two Numbers 
def addTwoNumbers(l1, l2):
    dn = ListNode(0)
    c = dn 
    cc = 0 
    while l1 or l2 or cc:
        x = l1.val if l1 else 0 
        y = l2.val if l2 else 0 
        s = x + y + cc
        cc = s // 10 
        c.next = ListNode(s%10)
        c = c.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None 
    return dn.next 

# 23 Merge K Sorted Lists 
def mergeKLists(lists):
    # Merge the Two Sorted Lists 
    def f(x,y):
        r = ListNode()
        c = r 
        while x and y:
            if x.val < y.val:
                c.next = x
                x = x.next 
            else:
                c.next = y 
                y = y.next 
            c = c.next 
        if x:
            c.next = x
        if y:
            c.next = y 
        return r.next 
    
    # Edge Case 
    if not lists:
        return None
    
    # Merge Two Lists At a Time Until Exausted 
    while len(lists) > 1:
        m = []
        for i in range(0,len(lists),2):
            x = lists[i]
            y = lists[i+1] if (i+1) < len(lists) else None
            m.append(f(x,y))
        lists = m 

    return lists[0] 

