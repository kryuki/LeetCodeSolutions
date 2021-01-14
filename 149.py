import math
from fractions import Fraction
from collections import defaultdict
from collections import Counter


class Solution:
    # solution1: calculate all the pairs and store the gradient into the hash map
    # time: O(N^2), space: O(N)
    def maxPoints(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        result = 0
        points = Counter(map(tuple, points))
        n = len(points)
        gradDic = defaultdict(int)

        while points and n >= result:
            startP, startCnt = points.popitem()
            n -= startCnt
            gradDic.clear()
            for endP, endCnt in points.items():
                numerator = endP[1] - startP[1]
                denominator = endP[0] - startP[0]
                grad = Fraction(
                    numerator, denominator) if denominator != 0 else math.inf
                gradDic[grad] += endCnt
            maxCnt = max(gradDic.values()) if gradDic else 0
            result = max(result, maxCnt + startCnt)

        return result
