class Solution:
    #solution1: brute force using stack
    #time: O(3^N * 4^M), space: O(3^N * 4^M)
    #(N: # of digits that maps to 3 letters, M: # of digits that maps to 4 letters)
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        output = []
        numDic = {"2": ["a", "b", "c"], "3": ["d", "e", "f"],
                  "4": ["g", "h", "i"], "5": ["j", "k", "l"], "6": ["m", "n", "o"],
                  "7": ["p", "q", "r", "s"], "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"]}
        button = numDic[digits[0]]
        for char in button:
            output.append(char)
        
        for i in range(1, len(digits)):
            numSoFar = len(output)
            digit = digits[i]
            button = numDic[digit]
            for j in range(numSoFar):
                wordSoFar = output.pop(0)
                for char in button:
                    newWord = wordSoFar + char
                    output.append(newWord)
            
        return output
    
    #solution2: backtrack
    #time: O(3^N * 4^M), space: O(3^N * 4^M)
    #(N: # of digits that maps to 3 letters, M: # of digits that maps to 4 letters)
    def letterCombinations2(self, digits: str) -> List[str]:
        if not digits:
            return []
        output = []
        numDic = {"2": ["a", "b", "c"], "3": ["d", "e", "f"],
                  "4": ["g", "h", "i"], "5": ["j", "k", "l"], "6": ["m", "n", "o"],
                  "7": ["p", "q", "r", "s"], "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"]}
        
        def backtrack(wordSoFar, idx):
            nonlocal output
            if idx == len(digits):
                output.append(wordSoFar)
            else:
                digit = digits[idx]
                button = numDic[digit]
                for char in button:
                    backtrack(wordSoFar + char, idx + 1)
        
        backtrack("", 0)
        return output