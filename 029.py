class Solution:
    def printAnswer(self, negative, quotient) -> int:
        minOverFlow, maxOverFlow = -2 ** 31, 2 ** 31 - 1
        if negative:
            quotient *= -1
        if quotient < minOverFlow:
            return minOverFlow
        elif quotient > maxOverFlow:
            return maxOverFlow
        else:
            return quotient

    def findBiggestDivisor(self, dividend, divisor):
        cur, quo = divisor, 1
        while cur + cur <= dividend:
            cur += cur
            quo += quo
        return [cur, quo]

    # solution1: Repeated Exponential Searches
    # time: O(logn * logn), space: O(1)
    def divide(self, dividend: int, divisor: int) -> int:
        negative = dividend * divisor < 0
        dividend, divisor = abs(dividend), abs(divisor)
        quotient, rest = 0, dividend

        while rest >= divisor:
            biggest, addQuo = self.findBiggestDivisor(rest, divisor)
            quotient += addQuo
            rest -= biggest

        return self.printAnswer(negative, quotient)

    # solution2: Adding Powers of Two
    # time: O(logn), space: O(logn)
    def divide2(self, dividend: int, divisor: int) -> int:
        negative = dividend * divisor < 0
        dividend, divisor = abs(dividend), abs(divisor)
        quotient, rest = 0, dividend
        powers = [[0, 1]]

        biggest, addQuo = self.findBiggestDivisor(rest, divisor)
        if rest >= biggest:
            quotient += addQuo
            rest -= biggest

        def findNextBiggestDivisor(rest, idx):
            while rest < powers[idx][1]:
                idx -= 1
            cur = powers[idx][1]
            quo = powers[idx][0]
            return [cur, quo, idx]

        idx = len(powers) - 1
        while rest >= divisor:
            nextBiggest, addQuo, idx = findNextBiggestDivisor(rest, idx)
            rest -= nextBiggest
            quotient += addQuo

        return self.printAnswer(negative, quotient)
