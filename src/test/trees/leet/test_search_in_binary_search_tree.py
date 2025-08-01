from trees.leet.search_in_binary_search_tree import search_bst
from trees.tree import TreeNode


class TestSearchInBST:
    def test_inorder_traversal_1(self):
        self.tree = TreeNode().create_bst([4, 2, 1, 3, 7])
        assert [2, 1, 3] == list(search_bst(self.tree, 2))

    def test_inorder_traversal_2(self):
        self.tree = TreeNode().create_bst([4, 2, 1, 3, 7])
        assert search_bst(self.tree, 5) is None

    def test_inorder_traversal_3(self):
        self.tree = TreeNode().create_bst([4, 2, 1, 3, 7])
        assert [3] == list(search_bst(self.tree, 3))

    def test_inorder_traversal_4(self):
        self.tree = TreeNode().create_bst([4, 2, 1, 3, 7])
        assert [4, 2, 1, 3, 7] == list(search_bst(self.tree, 4))
