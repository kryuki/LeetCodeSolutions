class Solution:
    #solution1: Hardcode digits
    #time: O(1), space: O(1)
    def intToRoman(self, num: int) -> str:
        output = ""
        L = len(str(num))
        for i in range(L):
            digit = int(str(num)[i])
            cnt_5, mod_5 = digit // 5, digit % 5
            add = ""
            if L - i == 1:
                if digit == 4:
                    add = "IV"
                elif digit == 9:
                    add = "IX"
                else:
                    add = cnt_5 * "V" + mod_5 * "I"
            elif L - i == 2:
                if digit == 4:
                    add = "XL"
                elif digit == 9:
                    add = "XC"
                else:
                    add = cnt_5 * "L" + mod_5 * "X"
            elif L - i == 3:
                if digit == 4:
                    add = "CD"
                elif digit == 9:
                    add = "CM"
                else:
                    add = cnt_5 * "D" + mod_5 * "C"
            else:
                #L - i == 4
                add = digit * "M"
            output += add
        
        return output