from collections import Counter


class Solution:
    # solution1: Using two sets and counter
    # time: O(m + n), space: O(m + n)
    def intersect(self, nums1, nums2):
        set1, set2 = set(nums1), set(nums2)
        counter1, counter2 = dict(Counter(nums1)), dict(Counter(nums2))
        intersect = set1.intersection(set2)
        output = []
        for num in intersect:
            cnt1, cnt2 = counter1[num], counter2[num]
            add = [num for _ in range(min(cnt1, cnt2))]
            output.extend(add)
        return output
