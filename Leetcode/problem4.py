# https://leetcode.com/problems/median-of-two-sorted-arrays/
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = self.merge_sorted_lists_concat_sort(nums1, nums2)
        list_len = len(merged)
        print(merged)
        if list_len % 2 == 0:
            median = ( merged[list_len//2-1] + merged[list_len//2] ) / 2
        else:
            median = merged[list_len//2]
        return median

    #less memory, more runtime
    def merge_sorted_lists_while(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        i = 0
        j = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                result.append(nums1[i])
                i += 1
            else:
                result.append(nums2[j])
                j += 1

        while i < len(nums1):
            result.append(nums1[i])
            i += 1

        while j < len(nums2):
            result.append(nums2[j])
            j += 1

        return result

    #more memory, less runtime
    def merge_sorted_lists_concat_sort(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = (nums1 + nums2)
        result.sort()
        return result

numbers1 = [1, 3]
numbers2 = [2, 4]

s = Solution()
median = s.findMedianSortedArrays(nums1=numbers1, nums2=numbers2)
print("Median:", median)
