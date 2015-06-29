class Stack:
    # initialize your data structure here.
    def __init__(self):
        self.data = []
        

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.data.append(x)

    # @return nothing
    def pop(self):
        if not self.empty():
            self.data.pop()
        

    # @return an integer
    def top(self):
        if not self.empty():
            return self.data[len(self.data) - 1 ]

    # @return an boolean
    def empty(self):
        return len(self.data) == 0 
        
