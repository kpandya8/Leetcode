# # Longest Palindromic Substring Medium

# # Given a string s, return the longest palindromic substring in s.

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"
 

# Constraints:

# 1 <= s.length <= 1000
# s consist of only digits and English letters.


# The understanding and approach: Make a DP tavle to save the strings and check for palindrome.
# Check for how can you move over one element, as its a true case for palindrome
# Reverse slicing is not true because might generate incomplete string. 
class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_palindrome =''
        dp = [[0]* len(s) for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
            longest_palindrome = s[i]
        
        for i in range(len(s)-1,-1,-1):
            for j in range (i+1,len(s)):
                if s[i] == s [j]:
                    if j-i == 1 or dp[i+1][j-1] is True:
                        dp[i][j] = True
                        if len(longest_palindrome) < len(s[i:j+1]):
                            longest_palindrome = s[i:j+1]
        
        return longest_palindrome
    
    def _main_(self):
        s="abcbader"
        print(self.longestPalindrome(s))

sol =Solution()
print(sol._main_())