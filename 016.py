import math
class Solution:
    #solution1: two pointers
    #time: O(n^2), space: O(logN) 
    #(depending on the implementation of the sorting algorithm)
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        bestSoFar = math.inf
        for i, num in enumerate(nums):
            if i >= len(nums) - 2: break
            closest = self.twoSumClosest(nums, i + 1, num, target)
            bestSoFar = self.updateValue(bestSoFar, closest, target)
            #found target!
            if bestSoFar == target: break
        return bestSoFar
    
    def twoSumClosest(self, nums, idx, num, target):
        l, r = idx, len(nums) - 1
        bestSoFar = math.inf
        while l < r:
            curSum = nums[l] + nums[r] + num
            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return curSum
            bestSoFar = self.updateValue(bestSoFar, curSum, target)
            
        return bestSoFar
    
    def updateValue(self, a, b, target):
        if abs(target - a) <= abs(target - b):
            return a
        else:
            return b