# 22. Generate Parentheses
# Medium
# Topics
# Companies
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:

# Input: n = 1
# Output: ["()"]

from typing import List

class Solution:
    def parentheses(self, n:int)->List[str]:
        output = []

        def rec(left, right, stack, cand):
            if left == right == 0:
                output.append(cand)
                return

            if left > 0:
                rec(left-1, right,stack+1,cand+"(")
            if right > 0 and stack > 0:
                rec(left, right-1, stack-1,cand+")")
            
        rec(n,n,0,"")

        return output
sol = Solution()
print(sol.parentheses(4))