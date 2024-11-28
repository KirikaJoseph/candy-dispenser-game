class Stack:
    def __init__(self, max_size=10):
        """Initialize the stack with a maximum size."""
        self.stack = []
        self.max_size = max_size

    def push(self, item):
        """Add an item to the stack if it's not full."""
        if len(self.stack) < self.max_size:
            self.stack.append(item)
            return True  # Success
        else:
            print("Stack is full!")
            return False  # Fail

    def pop(self):
        """Remove and return the top item of the stack."""
        if self.stack:
            return self.stack.pop()  # Success
        else:
            print("Stack is empty!")
            return None  # Fail

    def peek(self):
        """View the top item of the stack without removing it."""
        if self.stack:
            return self.stack[-1]
        else:
            print("Stack is empty!")
            return None

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.stack) == 0

    def is_full(self):
        """Check if the stack is full."""
        return len(self.stack) == self.max_size

    def size(self):
        """Get the current size of the stack."""
        return len(self.stack)
    def clear(self):
        """Clear the stack."""
        self.stack = [] 
