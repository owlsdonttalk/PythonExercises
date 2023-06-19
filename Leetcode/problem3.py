# https://leetcode.com/problems/longest-substring-without-repeating-characters/
import string
from typing import Optional


class Solution:
    def lengthOfLongestSubstring(self, s: string) -> Optional[int]:
        if len(s) < 1:
            return 0

        longest = 0

        for index, symbol in enumerate(s):
            longest_cur_substring = self.checkLongestSubstring(s[index:])
            if longest_cur_substring > longest:
                longest = longest_cur_substring
            # print(s[index:],longest_cur_substring)


        return longest

    def checkLongestSubstring(self, s: string):
        cur_substring = {}
        for symbol in s:
            if symbol in cur_substring:
                return len(cur_substring)
            else:
                cur_substring[symbol] = None
        return len(cur_substring)


str = 'pwwkew'
s = Solution()
print(s.lengthOfLongestSubstring(str))
