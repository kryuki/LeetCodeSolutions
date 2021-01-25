class Solution:
    #solution1: using stack
    #time: O(N), space: O(N)
    def isValid(self, s: str) -> bool:
        brackets = {"(" : ")", "{" : "}", "[" : "]"}
        openBrackets, closeBrackets = brackets.keys(), brackets.values()
        
        stack = []
        for char in s:
            if char in openBrackets:
                stack.append(char)
            else:
                if not stack:
                    return False
                else:
                    pop = stack.pop()
                    if brackets[pop] != char:
                        return False
        return not stack