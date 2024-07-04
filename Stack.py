class StackList:
    def __init__(self):
        self.stack = []

    def push(self, item):
        """Pushes an item onto the stack."""
        self.stack.append(item)

    def pop(self):
        """Removes and returns the last item from the stack. Raises an error if the stack is empty."""
        if self.is_empty():
            raise IndexError("Pop from an empty stack")
        return self.stack.pop()

    def peek(self):
        """Returns the last item from the stack without removing it. Raises an error if the stack is empty."""
        if self.is_empty():
            raise IndexError("Peek from an empty stack")
        return self.stack[-1]

    def is_empty(self):
        """Returns True if the stack is empty, False otherwise."""
        return len(self.stack) == 0

    def size(self):
        """Returns the number of items in the stack."""
        return len(self.stack)


####-------------------------------------------------------------

from collections import deque

class StackDeque:
    def __init__(self):
        self.stack = deque()

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from an empty stack")
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from an empty stack")
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)




# Example usage
if __name__ == "__main__":

    stack1 = StackList()
    stack1.push(1)
    stack1.push(2)
    stack1.push(3)
    print(stack1.pop())    # Output: 3
    print(stack1.peek())   # Output: 2
    print(stack1.size())   # Output: 2
    print(stack1.is_empty())  # Output: False


    # Example usage
    stack2 = StackDeque()
    stack2.push(1)
    stack2.push(2)
    stack2.push(3)
    print(stack2.pop())    # Output: 3
    print(stack2.peek())   # Output: 2
    print(stack2.size())   # Output: 2
    print(stack2.is_empty())  # Output: False