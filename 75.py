class Solution:
    #solution1: delete and append/insert
    # time: O(N) space: O(1)
    def sortColors(self, nums: list[int]) -> None:
        idx = 0
        for _ in nums:
            curNum = nums[idx]
            if curNum == 0:
                del nums[idx]
                nums.insert(0, 0)
                idx += 1
            elif curNum == 2:
                del nums[idx]
                nums.append(2)
            else:
                #curNum == 1
                idx += 1
