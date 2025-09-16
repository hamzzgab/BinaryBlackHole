def inorder_traversal(root):
    res = []

    def inorder(node):
        if not node:
            return

        inorder(node.left)
        res.append(node.val)
        inorder(node.right)

    inorder(root)
    return res
