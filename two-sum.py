# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]

# Constraints:

# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.

# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

# Approaches: (1) Brute Force. (2) Two Pass Hash Table. (3) One Pass Hash Table. 
# (1) Brute Force: The brute force approach is simple. Loop through each element xxx and find if there is another value that equals to target−xtarget - xtarget−x.
# initialize the loop in range for number of items in the list, so we start with i and the range is the number of elements in the list
# 
### Solution:

#Given: 
from typing import List  #Need to import List or else it will throw an error

class Solution:
    def twoSum_bruteForce(self, nums: List[int], target: int) -> List[int]:
        #Code written:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i,j]

    def twoSum_twoWayHashTable(self, nums: List[int], target: int) -> List[int]:
        #Code written:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return [i. hashmap[complement]]
    
    def twoSum_oneWayHashTable(self, nums: List[int], target: int) -> List[int]:
        #Code written:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i

    def _main_(self):
        print(self.twoSum_bruteForce([2,3,4],7)) #TC: n^2, #SC: 1
        print(self.twoSum_twoWayHashTable([2,3,4],7)) #TC: n, SC: n
        print(self.twoSum_oneWayHashTable([2,3,4], 7)) #TC: n, SC: n

sol = Solution()
print(sol._main_()) 
