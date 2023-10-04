# Median of Two Sorted Arrays
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).

# Example 1:

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.

# Example 2:

# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

# Constraints:

# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -106 <= nums1[i], nums2[i] <= 106

# My logic and understanding: The first approach is to merge the two arrays and then find the middle element from the merged array. Also cosider the odd and even factor.


class Solution:
    def median_of_the_given_arrays(self, nums1: list[int], nums2: list[int]) -> float:
        merge_two_arrays = nums1 + nums2
        merge_two_arrays.sort()

        total = len(merge_two_arrays)

        # odd number of elements
        if total % 2 == 1:
            return float(merge_two_arrays[total//2])
        else:
            m1 = merge_two_arrays[total // 2 - 1]
            m2 = merge_two_arrays[total // 2]
            return (float(m1) + float(m2)) // 2.0
    
    def _main_(self):
        a = [1]
        b = [3]
        print(self.median_of_the_given_arrays(a,b))


sol = Solution()
print(sol._main_())
