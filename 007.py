class Solution:
    # solution1: change to string and reverse
    # time: O(logx), O(logx)
    def reverse(self, x: int) -> int:
        rangeMin, rangeMax = -2 ** 31, 2 ** 31 - 1
        s = str(x)
        if x < 0:
            s = "-" + s[1:][::-1]
        else:
            s = s[::-1]
        return int(s) if rangeMin <= int(s) <= rangeMax else 0
