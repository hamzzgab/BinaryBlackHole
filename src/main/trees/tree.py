from treelib import Tree


class TreeNode:
    def __init__(self, left=None, val=None, right=None):
        self.left = left
        self.val = val
        self.right = right

    def insert_bst(self, val):
        if val < self.val:
            if self.left:
                self.left.insert_bst(val)
            else:
                self.left = TreeNode(val=val)
        else:
            if self.right:
                self.right.insert_bst(val)
            else:
                self.right = TreeNode(val=val)

    @staticmethod
    def create_bst(pre_order):
        if not pre_order:
            return

        root = TreeNode(val=pre_order[0])

        for val in pre_order[1:]:
            root.insert_bst(val)

        return root

    def display(self):  # pragma: no cover
        tree = Tree()
        self._add(tree, self)
        tree.show(sorting=False)

    def _add(self, tree, node, parent_id=None):  # pragma: no cover
        if not node:
            return

        label = str(node.val)
        node_id = str(id(node))

        tree.create_node(tag=label,
                         identifier=node_id,
                         parent=parent_id)
        if node.left:
            self._add(tree=tree, node=node.left, parent_id=node_id)
        if node.right:
            self._add(tree=tree, node=node.right, parent_id=node_id)

    def __iter__(self):
        yield self.val
        if self.left:
            yield from self.left
        if self.right:
            yield from self.right
