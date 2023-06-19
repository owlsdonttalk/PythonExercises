# https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s

        longest = ''

        for index, symbol in enumerate(s):
            for i in range(index, len(s)):
                substring = s[index:i+1]
                if self.is_polindrime_algorythm(substring):
                    if len(substring) > len(longest):
                        longest = substring

        return longest

    @staticmethod
    def is_polindrime_python(str):
        return str == str[::-1]

    @staticmethod
    def is_polindrime_while(string):
        left = 0
        right = len(string) - 1
        while left < right:
            if string[left] != string[right]:
                return False
            left += 1
            right -= 1

        return True


s = Solution
t = s.longestPalindrome(s='bb', self=s)
print(t)
