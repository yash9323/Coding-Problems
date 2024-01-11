# Neet Code Binary Search 
import math 

# 704 Binary Search 
def search(nums, target):
    start, end = 0, len(nums) - 1
    while start <= end :
        mid = (start + end) // 2
        if nums[mid] == target:
            return mid 
        if nums[mid] < target:
            start = mid + 1
        if nums[mid] > target:
            end = mid - 1
    return -1 

# 74 Search A 2D Matrix 
def searchMatrix(matrix, target):
        def search(nums, target):
            start, end = 0, len(nums) - 1
            while start <= end :
                mid = (start + end) // 2
                if nums[mid] == target:
                    return mid 
                if nums[mid] < target:
                    start = mid + 1
                if nums[mid] > target:
                    end = mid - 1
            return -1 

        def f(matrix,target):
            start, end = 0, len(matrix) - 1 
            while start <= end:
                mid = (start+end) // 2
                if matrix[mid][0] <= target <= matrix[mid][-1]:
                    return mid 
                elif matrix[mid][0] > target:
                    end = mid - 1 
                elif matrix[mid][0] < target:
                    start = mid + 1 
            if start > end:
                return -1 
            return mid

        r = f(matrix,target) 
        if r == -1:
            return False
        c = search(matrix[r],target)
        if c == -1:
            return False 
        return True

# 875 KOKO Eating Bananas 
def minEatingSpeed(piles, h):
    i, j = 1, max(piles)
    while i < j :
        mid = (i+j) // 2
        s = 0 
        for ii in piles:
            s += math.ceil(ii / mid)
        if s <= h:
            j = mid 
        else:
            i = mid + 1
    return j 

# 153 Find Minimum in roated sorted array 
def findMin(nums):
    i, j = 0, len(nums) - 1 
    while i < j:
        mid = (i+j) // 2
        if nums[mid] > nums[j]:
            i = mid + 1
        else:
            j = mid 
    return nums[i]

# 33 Search Rotated Array 
def search(nums, target):
    i, j = 0, len(nums) - 1
    while i <= j:
        mid = (i+j)//2
        if nums[mid] == target:
            return mid 
        if nums[i] <= nums[mid]:
            if nums[i] <= target < nums[mid]:
                j = mid - 1 
            else:
                i = mid + 1 
        else:
            if nums[mid] < target <= nums[j]:
                i = mid + 1 
            else:
                j = mid - 1
    return -1 

# 981 Time Based Key-Vlaue Store 
class TimeMap:
    def __init__(self):
        self.store = {}
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key] = self.store.get(key,[]) + [[value,timestamp]]
    def get(self, key: str, timestamp: int) -> str:
        out = ""
        data = self.store.get(key,[])
        i, j = 0, len(data) - 1
        while i <= j:
            mid = (i+j) // 2
            if data[mid][1] <= timestamp:
                out = data[mid][0]
                i = mid + 1 
            else:
                j = mid - 1 
        return out 
    
# 4 Median of two Sorted Arrays 
def findMedianSortedArrays(nums1, nums2):
    if len(nums2) < len(nums1):
        nums1,nums2 = nums2,nums1
    t = len(nums1) + len(nums2)
    h = t // 2
    i , j = 0, len(nums1) - 1
    while True:
        mida = (i+j) // 2
        midb = h - mida - 2
        la = nums1[mida] if mida >= 0 else float("-infinity")
        ra = nums1[mida+1] if mida+1 < len(nums1)  else float("infinity")
        lb = nums2[midb] if midb >=0 else float("-infinity")
        rb = nums2[midb+1] if midb+1 < len(nums2) else float("infinity")
        if la <= rb and lb <= ra:
            if t%2:
                return min(ra,rb)
            return (max(la,lb) + min(ra,rb)) / 2
        elif la > rb:
            j = mida - 1
        else:
            i = mida + 1