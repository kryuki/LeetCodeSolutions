class Solution:
    # solution 1 Using two sets
    # time O(n + m), space O(n + m)
    def intersection(self, nums1, nums2):
        set1, set2 = set(nums1), set(nums2)
        intersect = set1.intersection(set2)
        return list(intersect)
