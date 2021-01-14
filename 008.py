class Solution:
    # solution1: check each digit
    # time: O(N), space: O(1)
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0

        # handle operator
        sign = -1 if s[0] == "-" else 1
        if s[0] in ["-", "+"]:
            s = s[1:]

        num = sign * self.getLongestNum(s)
        return self.clamp(num, -2 ** 31, 2 ** 31 - 1)

    def getLongestNum(self, s):
        idx = 0
        while idx < len(s) and s[idx].isdigit():
            idx += 1
        return int(s[:idx]) if idx != 0 else 0

    def clamp(self, num, minRange, maxRange):
        if num < minRange:
            return minRange
        elif num > maxRange:
            return maxRange
        else:
            return num
