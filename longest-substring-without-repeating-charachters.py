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

# Three approaches: 1) Brute Force, 2) Slide Window, 3) HashMap

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


    def _main_(self):
        s="pwwkew"
        return self.lengthOfLongestSubstring_bruteforce(s)

sol = Solution()
print(sol._main_())