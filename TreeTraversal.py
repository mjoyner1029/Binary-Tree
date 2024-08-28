class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def in_order_traversal(self, node):
        """Traverse the tree in in-order (Left, Root, Right)."""
        if node is not None:
            self.in_order_traversal(node.left)
            print(node.value, end=' ')
            self.in_order_traversal(node.right)

    def pre_order_traversal(self, node):
        """Traverse the tree in pre-order (Root, Left, Right)."""
        if node is not None:
            print(node.value, end=' ')
            self.pre_order_traversal(node.left)
            self.pre_order_traversal(node.right)

    def post_order_traversal(self, node):
        """Traverse the tree in post-order (Left, Right, Root)."""
        if node is not None:
            self.post_order_traversal(node.left)
            self.post_order_traversal(node.right)
            print(node.value, end=' ')

def test_tree_traversals():
    # Create the binary tree structure
    # Binary Tree:
    #               50
    #        ┌─────┴─────┐
    #       30           70
    #    ┌────┴────┐   ┌────┴────┐
    #   40         20  60        80

    root = TreeNode(50)
    root.left = TreeNode(30)
    root.right = TreeNode(70)
    root.left.left = TreeNode(40)
    root.left.right = TreeNode(20)
    root.right.left = TreeNode(60)
    root.right.right = TreeNode(80)

    tree = BinaryTree(root)

    # Testing in-order traversal
    print("In-Order Traversal:")
    tree.in_order_traversal(tree.root)
    print()

    # Testing pre-order traversal
    print("Pre-Order Traversal:")
    tree.pre_order_traversal(tree.root)
    print()

    # Testing post-order traversal
    print("Post-Order Traversal:")
    tree.post_order_traversal(tree.root)
    print()

if __name__ == "__main__":
    test_tree_traversals()
