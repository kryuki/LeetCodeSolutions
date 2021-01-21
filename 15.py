class Solution:
    #solution1: sort & two pointers
    #time: O(N^2), space: O(logN) (depending on how you sort)
    #we ignore the memory required for the output
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        nums.sort()
        outputSet = set()
        for i, num in enumerate(nums):
            if i >= len(nums) - 2:
                break
            target = -num
            outputSet |= self.twoSum(nums, i + 1, target)
        
        return [list(item) for item in outputSet]
    
    def twoSum(self, nums, idx, target):
        l, r = idx, len(nums) - 1
        output = set()
        while l < r:
            curSum = nums[l] + nums[r]
            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                ansTuple = (-target, nums[l], nums[r])
                output.add(ansTuple)
                l += 1
                r -= 1
        return output