class Solution:
    # solution1: vertical scanning
    # time: O(S), space: O(1) (S = sum of the letters)
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ""
        idx = 0
        while self.checkAllIdx(strs, idx):
            idx += 1
        return strs[0][:idx] if idx else ""

    def checkAllIdx(self, strs, idx):
        if idx >= len(strs[0]): return False

        commonChar = strs[0][idx]
        for s in strs:
            if idx >= len(s) or s[idx] != commonChar:
                return False
        return True

    # solution2: horizontal scanning
    # time: O(S), space: O(1) (S = sum of the letters)
    def longestCommonPrefix2(self, strs: List[str]) -> str:
        if not strs: return ""
        longestCommonSoFar = strs[0]

        for i in range(1, len(strs)):
            longestCommonSoFar = self.longestCommon(longestCommonSoFar, strs[i])
            if not longestCommonSoFar:
                break

        return longestCommonSoFar

    def longestCommon(self, str1, str2):
        idx = 0
        while idx < len(str1) and idx < len(str2) and str1[idx] == str2[idx]:
            idx += 1
        return str1[:idx]