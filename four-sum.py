# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.

 

# Example 1:

# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
# Example 2:

# Input: nums = [2,2,2,2,2], target = 8
# Output: [[2,2,2,2]]
 

# Constraints:

# 1 <= nums.length <= 200
# -109 <= nums[i] <= 109
# -109 <= target <= 109

from typing import List  #Need to import List or else it will throw an error

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()

        ans = []
        unique_set = set()

        for i in range(n):
            for j in range(i + 1, n):
                k = j + 1
                l = n - 1

                while k < l:
                    total_sum = nums[i] + nums[j] + nums[k] + nums[l]

                    if total_sum == target:
                        temp = [nums[i], nums[j], nums[k], nums[l]]
                        unique_set.add(tuple(temp))
                        k += 1
                        l -= 1
                    elif total_sum < target:
                        k += 1
                    elif total_sum > target:
                        l -= 1

        ans = list(unique_set)
        return ans
    
sol = Solution()
print(sol.fourSum(nums=[1,1,1,2,2],target= 6))
print(sol.fourSum([1,0,-1,-2,2],target=0))