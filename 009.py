class Solution:
    # solution1: revert the number
    # time: O(logx), space: O(1)
    def isPalindrome(self, x: int) -> bool:
        if x == 0:
            return True
        if x < 0:
            return False
        if x % 10 == 0:
            return False
        inverseNum = 0
        cur = x
        while cur:
            inverseNum = inverseNum * 10 + cur % 10
            cur //= 10
        return x == inverseNum

    # solution2: convert to string
    # time: O(logx), space: O(logx)
    def isPalindrome2(self, x: int) -> bool:
        return str(x) == str(x)[::-1]
