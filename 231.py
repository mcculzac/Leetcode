# https://leetcode.com/problems/power-of-two/
# Given an integer n, return true if it is a power of two. Otherwise, return false.

# An integer n is a power of two, if there exists an integer x such that n == 2x.

 

# Example 1:

# Input: n = 1
# Output: true
# Explanation: 2^0 = 1
# Example 2:

# Input: n = 16
# Output: true
# Explanation: 2^4 = 16
# Example 3:

# Input: n = 3
# Output: false
 

# Constraints:

# -2^31 <= n <= 2^31 - 1
 

# Follow up: Could you solve it without loops/recursion?
import math
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 1:
            return False
        calculated = math.log(n, 2)
        float_detection = calculated % 1
        return float_detection < 1e-10
    def alternateIsPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n.bit_count() == 1


s = Solution()
tests = {
    0: False,
    1: True,
    3: False,
    8: True,
    16: True,
    16777217: False,
    536870912: True
}

print('\n'.join(f'{key}: {s.alternateIsPowerOfTwo(key)}| {tests[key]}' for key in tests))
