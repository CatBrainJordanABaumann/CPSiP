class Counter:
    def __init__(self):
        self._limit = 0

    def getValue(self) -> int:
        return len(self._strokes)
    
    def click(self):
        self._strokes += "|"
        if self.getValue() > self._limit:
            print("Limit Exceeded")
    
    def reset(self):
        self._strokes = ""
    
    def setLimit(self, maximum: int):
        self._limit = maximum