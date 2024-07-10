class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            raise IndexError("dequeue from an empty queue")

    def size(self):
        return len(self.queue)

# Example usage:
q = Queue()
q.enqueue(1)
q.enqueue(2)
print(q.dequeue())  # Output: 1
print(q.size())     # Output: 1