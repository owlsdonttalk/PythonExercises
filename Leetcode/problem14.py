from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = []

        num = len(strs)
        for x in zip(*strs):
            if len(set(x)) == 1:
                prefix.append(x[0])
            else:
                break

        return "".join(prefix)


strs = ["flower","flow","flight"]
s = Solution
print(s.longestCommonPrefix(s, strs))