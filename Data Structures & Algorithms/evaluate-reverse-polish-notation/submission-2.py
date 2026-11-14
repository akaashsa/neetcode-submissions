class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # if number store
        # if digit then take out first two process and store
        # if only one left than return or invalid

        ans = 0
        stack = []
        for i in tokens:
            if i not in "+-/*":
                stack.append(int(i))
            
            else:
                num1 = stack.pop()
                num2 = stack.pop()
               
                if i == '+':
                    stack.append(num1+num2)

                if i == '-':
                    stack.append(num2-num1)
                if i == '/':
                  div = num2/num1
                  stack.append(math.floor(div) if div>=0 else math.ceil(div))
                
                if i == '*':
                    stack.append(num1*num2)

        
        return stack.pop() if stack else None