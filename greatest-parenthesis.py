# Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses 
# substring
# .

 

# Example 1:

# Input: s = "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()".
# Example 2:

# Input: s = ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()".
# Example 3:

# Input: s = ""
# Output: 0
 

# Constraints:

# 0 <= s.length <= 3 * 104
# s[i] is '(', or ')'.

class Solution:
    def longestValidParenthesis(self, s: str) -> int:
        stack = [-1]  # Initialize stack with -1 as the base index
        max_length = 0
        
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)  # Push the index of '(' to the stack
            else:
                stack.pop()  # Pop the top index from the stack
                
                if len(stack) == 0:
                    stack.append(i)  # Push the current index to the stack as the new base
                else:
                    max_length = max(max_length, i - stack[-1])  # Calculate the length of the valid substring
        
        return max_length
    
s = Solution()
print(s.longestValidParenthesis("(()"))
