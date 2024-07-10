class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def remove_child(self, child_node):
        self.children = [child for child in self.children if child != child_node]

    def __repr__(self):
        return f"TreeNode({self.value})"

# Example usage:
root = TreeNode("root")
child1 = TreeNode("child1")
child2 = TreeNode("child2")

root.add_child(child1)
root.add_child(child2)

root.remove_child(child1)
print(root.children)  # [TreeNode(child2)]