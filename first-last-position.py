# Find First and Last Position of Element in Sorted Array
class Solution:
    def searchRange(self, nums, target):
        # Find the first occurrence of the target
        first = self.findFirst(nums, target)
        
        # Find the last occurrence of the target
        last = self.findLast(nums, target)
        
        return [first, last]
    
    def findFirst(self, nums, target):
        left, right = 0, len(nums) - 1
        first = -1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
            
            if nums[mid] == target:
                first = mid
        
        return first
    
    def findLast(self, nums, target):
        left, right = 0, len(nums) - 1
        last = -1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
            
            if nums[mid] == target:
                last = mid
        
        return last