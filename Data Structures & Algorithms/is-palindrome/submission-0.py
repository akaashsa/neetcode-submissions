class Solution:
    def isPalindrome(self, s: str) -> bool:


        i =0
        j = len(s)-1
        #only consider alphanumeric if not increment/decrement that pointer by 1
        #end condition i>j --> return
        #only increment if both word same

        while i<=j:


          
                while i<j and not s[i].isalnum():
                    i += 1

                while i<j and not s[j].isalnum():
                    j -= 1

                if s[i].lower()==s[j].lower():
                    i += 1
                    j -= 1
                
                else : 
                    return False
        
        return True
            
            
