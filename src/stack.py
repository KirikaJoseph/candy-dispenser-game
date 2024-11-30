class Stack:
    def __init__(self, max_size=8):
        self.stack = []
        self.max_size = max_size

    def push(self, item):
        if len(self.stack) < self.max_size:
            self.stack.append(item)
            return True  
        else:
            print("Stack is full!")
            return False  # Fail

    def pop(self):
        if self.stack:
            return self.stack.pop()  # Success
        else:
            print("Stack is empty!")
            return None  # Fail

    def peek(self):
        if self.stack:
            return self.stack[-1]
        else:
            print("Stack is empty!")
            return None

    def is_empty(self):
        return len(self.stack) == 0

    def is_full(self):
        return len(self.stack) == self.max_size

    def size(self):
        return len(self.stack)
    def clear(self):
        self.stack = [] 
