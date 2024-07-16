class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._insert(node.right, key)

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

    def inorder(self):
        return self._inorder(self.root)

    def _inorder(self, node):
        if node:
            return self._inorder(node.left) + [node.key] + self._inorder(node.right)
        else:
            return []

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return node
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            min_larger_node = self._find_min(node.right)
            node.key = min_larger_node.key
            node.right = self._delete(node.right, min_larger_node.key)
        return node

    def _find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
    

# Create the BST
bst = BinarySearchTree()

# Insert elements
# bst.insert(50)
# bst.insert(30)
# bst.insert(70)
# bst.insert(20)
# bst.insert(40)
# bst.insert(60)
# bst.insert(80)

bst.insert(1)
bst.insert(2)
bst.insert(3)
bst.insert(6)
bst.insert(7)
bst.insert(9)

# Search for an element
result = bst.search(70)
print("Found:", result.key if result else "Not found")

# Print inorder traversal
print("Inorder traversal:", bst.inorder())

# Delete an element
bst.delete(70)
print("Inorder traversal after deleting 70:", bst.inorder())