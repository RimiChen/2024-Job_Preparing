class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def add(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BinaryTreeNode(value)
            else:
                self.left.add(value)
        else:
            if self.right is None:
                self.right = BinaryTreeNode(value)
            else:
                self.right.add(value)

    def find_min(self):
        current = self
        while current.left is not None:
            current = current.left
        return current

    def delete(self, value):
        if value < self.value:
            if self.left:
                self.left = self.left.delete(value)
        elif value > self.value:
            if self.right:
                self.right = self.right.delete(value)
        else:
            # Node with only one child or no child
            if self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            
            # Node with two children
            temp = self.right.find_min()
            self.value = temp.value
            self.right = self.right.delete(temp.value)
        return self

    def __repr__(self):
        return f"BinaryTreeNode({self.value})"

# Example usage:
root = BinaryTreeNode(10)
root.add(5)
root.add(15)
root.add(3)
root.add(7)

root = root.delete(5)
print(root.left)  # Should show the updated left subtree