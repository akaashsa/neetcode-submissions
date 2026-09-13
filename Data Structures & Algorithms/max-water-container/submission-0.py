class Solution:
    def maxArea(self, heights: List[int]) -> int:
       i = 0
       j = len(heights)-1
       maxArea = 0
       while i < j:

        height = min(heights[i],heights[j])
        width = j-i
        maxArea = max(height*width,maxArea)

        if heights[i]>heights[j]:
            j -=1
        else : 
            i +=1

    
       return maxArea

        
