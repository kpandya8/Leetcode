# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
 

# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters.
from typing import List  #Need to import List or else it will throw an error

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # index string i in array as 0, pasre through the entire string and compare elements 
        # if overlap, store info
        # another hint, we need prefix, so if starting dont match we retun ""
        # Better approach, sort the array, compare first and last value, if not same  return null, if same append string for all same charachters
    
        ans=""
        strs=sorted(strs)
        first=strs[0]
        last=strs[-1]
        for i in range(min(len(first),len(last))):
            if(first[i]!=last[i]):
                return ans
            ans+=first[i]
        return ans 
    
sol = Solution()
print(sol.longestCommonPrefix(["floor","flower","flyer"]))
    
