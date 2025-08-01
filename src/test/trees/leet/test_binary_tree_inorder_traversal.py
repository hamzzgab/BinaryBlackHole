from trees.tree import TreeNode
from trees.leet.binary_tree_inorder_traversal import inorder_traversal


class TestBSTInorderTraversal:
    def test_inorder_traversal_1(self):
        self.tree = TreeNode().create_bst([1, 2, 3])
        assert [1, 2, 3] == inorder_traversal(self.tree)

    def test_inorder_traversal_2(self):
        self.tree = TreeNode().create_bst([1])
        assert [1] == inorder_traversal(self.tree)

    def test_inorder_traversal_3(self):
        self.tree = TreeNode().create_bst([])
        assert [] == inorder_traversal(self.tree)

    def test_inorder_traversal_4(self):
        self.tree = TreeNode().create_bst([6, 4, 2, 1, 5, 9, 8, 7, 10])
        assert [1, 2, 4, 5, 6, 7, 8, 9, 10] == inorder_traversal(self.tree)
