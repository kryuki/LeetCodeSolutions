class Solution:
    # solution1: storing the last index found in the dictionary
    # time: O(n), space: O(n)
    def lengthOfLongestSubstring(self, s: str) -> int:
        idxDict = dict()
        startIdx, curL = 0, 0
        result = 0
        for i, char in enumerate(s):
            if char not in idxDict or idxDict[char] < startIdx:
                idxDict[char] = i
                curL += 1
                result = max(result, curL)
            else:
                startIdx = idxDict[char] + 1
                curL = i - startIdx + 1
                idxDict[char] = i
        return result

    # solution2: use two indexes and set
    # time: O(n), space: O(n)
    def lengthOfLongestSubstring2(self, s: str) -> int:
        foundChar = set()
        startIdx, endIdx, curL = 0, 0, 0
        result = 0
        while startIdx < len(s):
            if endIdx < len(s) and s[endIdx] not in foundChar:
                foundChar.add(s[endIdx])
                curL = endIdx - startIdx + 1
                result = max(result, curL)
                endIdx += 1
            else:
                foundChar.remove(s[startIdx])
                startIdx += 1
        return result
