class Solution:
    # solution1: dynamic programming with full table
    # time: O(L1*L2), space: O(L1*L2)
    def minDistance(self, word1: str, word2: str) -> int:
        word1 = " " + word1
        word2 = " " + word2
        L1, L2 = len(word1), len(word2)
        dp = [[0 for _ in range(L2)] for _ in range(L1)]
        for i in range(L1):
            dp[i][0] = i
        for j in range(L2):
            dp[0][j] = j

        for i in range(1, L1):
            for j in range(1, L2):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    a, b, c = dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]
                    dp[i][j] = min(min(a, b), c) + 1
        return dp[-1][-1]

    # solution2: dynamic programming with optimized table
    # time: O(L1*L2), space: O(max(L1, L2))
    def minDistance2(self, word1: str, word2: str) -> int:
        word1 = " " + word1
        word2 = " " + word2
        if len(word1) < len(word2):
            word1, word2 = word2, word1
        L1, L2 = len(word1), len(word2)
        dp = [[0 for _ in range(L2)] for _ in range(2)]
        for i in range(L2):
            dp[0][i] = i
        for i in range(1, L1):
            dp[1][0] = i
            for j in range(1, L2):
                if word1[i] == word2[j]:
                    dp[1][j] = dp[0][j - 1]
                else:
                    a, b, c = dp[0][j], dp[1][j - 1], dp[0][j - 1]
                    dp[1][j] = min(min(a, b), c) + 1
            if i != L1 - 1:
                dp[0], dp[1] = dp[1], dp[0]
        return dp[-1][-1]
