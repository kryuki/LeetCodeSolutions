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
                try:
                    grad = Fraction(numerator, denominator)
                except:
                    grad = math.inf
                gradDic[grad] += endCnt
            if gradDic:
                maxValue = max(gradDic.values())
            else:
                maxValue = 0
            result = max(result, maxValue + startCnt)

        return result
