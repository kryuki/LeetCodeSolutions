class Solution:
    # solution1: check each starting point
    # time: O(N^2), space: O(1)
    def longestPalindrome(self, s: str) -> str:
        longestSoFar, bestR, bestL = 0, 0, 0
        for i in range(0, 2 * len(s) - 1):
            curIdx = i / 2
            l, r = self.getLongest(s, curIdx)
            length = r - l + 1
            if length > longestSoFar:
                longestSoFar = length
                bestR, bestL = r, l
        return s[bestL: bestR + 1]

    def getLongest(self, s, curIdx):
        if curIdx.is_integer():
            l, r = int(curIdx), int(curIdx)
        else:
            l, r = int(curIdx - 1/2), int(curIdx + 1/2)
        while 0 <= l and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return l + 1, r - 1

    # solution2: create new spaced string
    # time: O(N^2), space: O(1)
    def longestPalindrome2(self, s: str) -> str:
        spaced_s = " ".join(list(s))
        longestSoFar, bestR, bestL = 0, 0, 0
        for i in range(len(spaced_s)):
            length, l, r = self.countLongest(spaced_s, i)
            if length > longestSoFar:
                longestSoFar = length
                bestL, bestR = l, r
        return spaced_s[bestL: bestR + 1].replace(" ", "")

    def countLongest(self, s, i):
        length = 0 if s[i] == " " else 1
        l, r = i - 1, i + 1
        while 0 <= l and r < len(s) and s[l] == s[r]:
            if s[l] != " ":
                length += 2
            l -= 1
            r += 1
        return length, l + 1, r - 1
