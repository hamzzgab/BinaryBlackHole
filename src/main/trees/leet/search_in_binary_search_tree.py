def search_bst(root, val):
    if not root:
        return

    if val < root.val:
        return search_bst(root.left, val)
    elif val > root.val:
        return search_bst(root.right, val)

    return root
