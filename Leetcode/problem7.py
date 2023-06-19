# https://leetcode.com/problems/reverse-integer/description/
import math

class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 10 else 1
        x = abs(x)
        num = 0

        while x != 0:
            num = num * 10 + x % 10
            x = x // 10

        if num < -2147483647 or num > 2147483648:
            return 0

        return num * sign

s = Solution
s.reverse(s, -120)