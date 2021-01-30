class Solution:
    #solution1: cascade
    #time: O(N*2^N), space: O(N*2^N)
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        output = [[]]
        
        #output = [[], [1]]
        for num in nums: #2
            add = [] #add = [[2], [1, 2]]
            for pair in output:
                add.append(pair + [num])
            output += add
        
        return output

        
        
        
        
        