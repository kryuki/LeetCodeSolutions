class Solution:
    # solution1: vertical scanning
    # time: O(S), space: O(1) (S = sum of the letters)
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        idx = 0
        while self.checkAllIdx(strs, idx):
            idx += 1
        return strs[0][:idx] if idx else ""

    def checkAllIdx(self, strs, idx):
        if idx >= len(strs[0]):
            return False

        commonChar = strs[0][idx]
        for s in strs:
            if idx >= len(s) or s[idx] != commonChar:
                return False
        return True
