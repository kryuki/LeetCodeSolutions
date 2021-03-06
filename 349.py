class Solution:
    # solution1: Using two sets
    # time O(m + n), space O(m + n)
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        set1, set2 = set(nums1), set(nums2)
        intersect = set1.intersection(set2)
        return list(intersect)
