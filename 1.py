class Solution:
    # solution1: use hash map
    # time: O(N), space: O(N)
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        found, output = {}, []
        for i, num in enumerate(nums):
            lookFor = target - num
            if lookFor in found:
                output = [found[lookFor], i]
            else:
                found[num] = i
        return output

    # solution2: sort and sliding window
    # time: O(nlogn), space: O(1)
    def twoSum2(self, nums: list[int], target: int) -> list[int]:
        idxNums = [[num, i] for i, num in enumerate(nums)]
        idxNums.sort(key=lambda x: x[0])
        left, right = 0, len(nums) - 1
        output = []
        while left <= right:
            curSum = idxNums[left][0] + idxNums[right][0]
            if curSum > target:
                right -= 1
            elif curSum < target:
                left += 1
            else:
                output = [idxNums[left][1], idxNums[right][1]]
                break
        return output

    # solution3: brute force
    # time: O(n^2), space: O(1)
    def twoSum3(self, nums: list[int], target: int) -> list[int]:
        output = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    output = [i, j]
        return output
