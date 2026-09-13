class Solution:
    def isValid(self, string: str) -> bool:
        s= []
        s_map = {'}':'{',']':'[',')':'('}
        for c in string:
            
            if c in ('(','{','['):
                s.append(c)
            else:
               
                if len(s)==0:
                    return False
                else:
                    if (s[-1] == s_map[c]):
                        
                        s.pop()
                    else : 
                        return False
   
        return len(s)==0