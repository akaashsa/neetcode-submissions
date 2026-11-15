class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #AABABACCACDAtk K =5
        mapWord = {}
        i = 0
        j = 0
        length = 1
        num = k
        while j < len(s):
            if s[j] in mapWord.keys():
                mapWord[s[j]] += 1
            
            else :
                mapWord[s[j]]=1

            diff = abs(max(mapWord.values())-(j-i+1))
        

            
            if diff >k :
                
                mapWord[s[i]] -=1
                i+=1
            length = max(length,j-i+1)
           
            j+= 1
        
        return length

