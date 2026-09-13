class MinStack:

    def __init__(self):
        self.minEl = []
        
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.stack :
            if self.minEl:
                if val<=self.minEl[-1] :
                    self.minEl.append(val)
            else:
                self.minEl.append(val)
            
            
        return None
        
    def pop(self) -> None:
      
            ele = self.stack.pop()
            if ele == self.minEl[-1]:
                self.minEl.pop()
            return ele
            return None

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        return None

    def getMin(self) -> int:
        if self.minEl :

            return self.minEl[-1]
        return None
