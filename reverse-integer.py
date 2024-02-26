# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

# Example 1:

# Input: x = 123
# Output: 321
# Example 2:

# Input: x = -123
# Output: -321
# Example 3:

# Input: x = 120
# Output: 21
 

# Constraints:

# -231 <= x <= 231 - 1

class Solution:
    def reverse_integer(self, x: int) -> int:
        upper_limit = (2 ** 31) -1
        is_negative = x < 0
        if is_negative:
            x = -x
        reverse = 0
        while x != 0:
            last_digit = x % 10
            if reverse > (upper_limit - last_digit) // 10:
                return 0
            reverse = reverse * 10 + last_digit
            x = x // 10
        if is_negative:
            reverse = -reverse
        return reverse

sol = Solution()
print(sol.reverse_integer(321))
print(sol.reverse_integer(-321))
print(sol.reverse_integer(3210))