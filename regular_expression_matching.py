# The matching should cover the entire input string (not partial).

 
# Example 1:

# Input: s = "aa", p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
# Example 2:

# Input: s = "aa", p = "a*"
# Output: true
# Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
# Example 3:

# Input: s = "ab", p = ".*"
# Output: true
# Explanation: ".*" means "zero or more (*) of any character (.)".
 

# Constraints:

# 1 <= s.length <= 20
# 1 <= p.length <= 20
# s contains only lowercase English letters.
# p contains only lowercase English letters, '.', and '*'.
# It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.

class Solution(object):
    def isMatch(self, text, pattern):
        if not pattern:
            return not text

        first_match = bool(text) and pattern[0] in {text[0], '.'}

        if len(pattern) >= 2 and pattern[1] == '*':
            return (self.isMatch(text, pattern[2:]) or
                    first_match and self.isMatch(text[1:], pattern))
            
        else:
            return first_match and self.isMatch(text[1:], pattern[1:])
        
sol = Solution()
print(sol.isMatch("aa","a."))