class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        setNums = {n for n in nums }

        ans = 0
        res = 1
        prev = list(setNums)[0]
        
        for i in setNums:
            if(i-1) not in setNums:
                length = 1

                while(i+length) in setNums:
                    length += 1
            
        
                ans = max(length,ans)
            
           

        return ans

            
