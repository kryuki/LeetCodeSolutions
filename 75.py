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

    # solution2: Dutch National Flag problem solution
    # time: O(N), space: O(1)
    def sortColors2(self, nums: list[int]) -> None:
        p0, cur = 0, 0
        p2 = len(nums) - 1

        while cur <= p2:
            curNum = nums[cur]
            if curNum == 0:
                nums[p0], nums[cur] = nums[cur], nums[p0]
                p0 += 1
                cur += 1
            elif curNum == 2:
                nums[cur], nums[p2] = nums[p2], nums[cur]
                p2 -= 1
            else:
                cur += 1
