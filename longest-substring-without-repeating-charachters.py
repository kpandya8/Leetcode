# Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without repeating characters.

# Example 1

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "abc", with the length of 1.

# Example 3

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring

# Constraints:

# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.

# Three approaches: 1) Brute Force, 2) Sliding Window, 3) HashMap
from collections import Counter #for sliding window
class Solution:
    def lengthOfLongestSubstring_bruteforce(self, s:str) -> int:
        def check(start, end):
            chars =  set()
            for i in range(start, end + 1):
                c = s[i]
                if c in chars:
                    return False
                chars.add(c)
            return True

        n = len(s)

        res = 0 
        for i in range(n):
            for j in range (i,n):
                if check(i,j):
                    res= max(res, j-i +1)
        return res

    def lengthOfLongestSubstring_slidingwindow(self, s:str) -> int:
        chars = Counter()

        left = right = 0
        res = 0
        while right< len(s):
            r = s[right]
            chars[r] +=1

            while chars[r] > 1:
                l = s[left]
                chars[l] -= 1
                left += 1

            res = max(res, right - left +1)

            right += 1
        return res
    
    def lengthOfLongestSubstring_hashMap(self, s:str) -> int:
        n = len(s)
        ans = 0
        # mp stores the current index of a character
        mp = {}

        i = 0
        # try to extend the range [i, j]
        for j in range(n):
            if s[j] in mp:
                i = max(mp[s[j]], i)
            ans = max(ans, j - i + 1)
            mp[s[j]] = j + 1

        return ans

    def _main_(self):
        s="pwwkew"
        print(self.lengthOfLongestSubstring_bruteforce(s)) #TC: O(n^3); SC: O(k)
        print(self.lengthOfLongestSubstring_slidingwindow(s)) #TC: O(2n) = O(n); SC: O(min(m,n))
        print(self.lengthOfLongestSubstring_hashMap(s)) #TC: O(n); SC: O(min(m,n))


sol = Solution()
print(sol._main_())