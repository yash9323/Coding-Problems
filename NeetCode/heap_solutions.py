# Neet Code Heaps 

import heapq

# 703 kth largest element in a stream 
class KthLargest:
    def __init__(self, k, nums):
        self.k = k 
        self.heap = nums 
        heapq.heapify(self.heap)
        while len(self.heap) > k:
            heapq.heappop(self.heap)
    def add(self, val: int) -> int:
        heapq.heappush(self.heap,val)
        while len(self.heap) > self.k :
            heapq.heappop(self.heap)
        return self.heap[0]
    
# 1046 Last Stone Weight 
def lastStoneWeight(stones):
    s = [-i for i in stones]
    heapq.heapify(s)

    while len(s) > 1:
        x = -1 * heapq.heappop(s)
        y = -1 * heapq.heappop(s)
        if x == y:
            continue 
        else:
            heapq.heappush(s,y-x)
    if s:
        return -s[0]
    else:
        return 0
    
# Kth Largest Element in a Array
def findKthLargest(nums, k):
    heapq.heapify(nums)
    while len(nums) > k:
        heapq.heappop(nums)
    return nums[0]

# 973 K Closest Point to the origin 
def kClosest(points, k):
    heap = []
    res = []
    heapq.heapify(heap)
    for point in points:
        d = ((point[0]**2)+(point[1]**2)) ** 0.5
        heapq.heappush(heap,(d,point))
    while k:
        d , p = heapq.heappop(heap)
        res.append(p)
        k -= 1
    return res

# 621 Task Scheduler 
def leastInterval(tasks, n):
    freq = {}
    heap = []
    q = []
    t = 0 
    heapq.heapify(heap)
    for task in tasks:
        freq[task] = 1 + freq.get(task,0) 
    for f in freq.values():
        heapq.heappush(heap,-f)
    while q or heap:
        t += 1 
        if heap:
            a = 1 + heapq.heappop(heap)
            if a:
                q.append([a,t+n])
        else:
            t = q[0][1]
        if q and q[0][1] == t:
            b = q.pop(0)
            heapq.heappush(heap,b[0])
    return t
        
# 355 Design Twitter 
class User:
    def __init__(self):
        self.posts = {}
        self.followers = set()
        self.following = set()

class Twitter:
    def __init__(self):
        self.time = 0 
        self.users = {}
    def create_user(self,userId):
        if userId not in self.users:
            self.users[userId] = User()
    def postTweet(self, userId: int, tweetId: int):
        self.time += 1
        self.create_user(userId)
        self.users[userId].posts[tweetId] = self.time
    def getNewsFeed(self, userId: int):
        feed = []
        heapq.heapify(feed)
        result = []
        self.create_user(userId)
        for owntweets in self.users[userId].posts:
            heapq.heappush(feed,[-self.users[userId].posts[owntweets],owntweets])
        for user in self.users[userId].following:
            for tweets in self.users[user].posts:
                heapq.heappush(feed,[-self.users[user].posts[tweets],tweets])
        while len(result) < 10:
            if feed:
                result.append(heapq.heappop(feed)[1])
            else:
                return result 
        return result 
    
    def follow(self, followerId: int, followeeId: int):
        self.create_user(followerId)
        self.create_user(followeeId)
        self.users[followerId].following.add(followeeId)
        self.users[followeeId].followers.add(followerId)
    def unfollow(self, followerId: int, followeeId: int):
        self.create_user(followerId)
        self.create_user(followeeId)
        self.follow(followerId,followeeId)
        self.users[followerId].following.remove(followeeId)
        self.users[followeeId].followers.remove(followerId)

# 295 Find Median from Data Stream 
class MedianFinder:
    def __init__(self):
        self.minheap = []
        self.maxheap = []
        heapq.heapify(self.minheap)
        heapq.heapify(self.maxheap)
    def addNum(self, num: int):
        if len(self.minheap) == len(self.maxheap):
            heapq.heappush(self.maxheap, -1 * heapq.heappushpop(self.minheap, -num))
        else:
            heapq.heappush(self.minheap, -1 * heapq.heappushpop(self.maxheap,num))
    def findMedian(self):
        if len(self.minheap) == len(self.maxheap):
            return (self.maxheap[0] - self.minheap[0]) / 2
        else:
            return self.maxheap[0]