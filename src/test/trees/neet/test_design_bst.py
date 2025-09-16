from trees.neet.design_bst import TreeMap


class TestDesignBst:
    def test_initial_tree_is_none(self):
        self.tree = TreeMap()
        assert not self.tree.root

    def test_insert_when_no_keys(self):
        self.tree = TreeMap().insert(key=1, val=100)
        assert self.tree.root.key == 1
        assert self.tree.root.val == 100

    def test_insert_when_key_greater(self):
        self.tree = TreeMap().insert(key=1, val=100).insert(key=2, val=200)
        assert self.tree.root.right.key == 2
        assert self.tree.root.right.val == 200

    def test_insert_when_key_lesser(self):
        self.tree = TreeMap().insert(key=3, val=300).insert(key=2, val=200)
        assert self.tree.root.left.key == 2
        assert self.tree.root.left.val == 200

    def test_insert_when_key_equal(self):
        self.tree = TreeMap().insert(key=1, val=10).insert(key=1, val=100)
        assert self.tree.root.key == 1
        assert self.tree.root.val == 100

    def test_get_when_empty(self):
        self.tree = TreeMap()
        assert self.tree.get(1) == -1

    def test_get_key(self):
        self.tree = TreeMap()
        self.tree.insert(key=3, val=300).insert(key=1, val=100).insert(key=2, val=200)
        assert self.tree.get(1) == 100
        assert self.tree.get(2) == 200
        assert self.tree.get(3) == 300

    def test_get_min(self):
        self.tree = TreeMap()
        assert self.tree.get_min() == -1

        self.tree.insert(key=2, val=2).insert(key=11, val=11).insert(key=31, val=31)
        assert self.tree.get_min() == 2

    def test_get_max(self):
        self.tree = TreeMap()
        assert self.tree.get_max() == -1
        self.tree.insert(key=2, val=2).insert(key=11, val=11).insert(key=31, val=31)
        assert self.tree.get_max() == 31

    def test_inorder_traversal(self):
        self.tree = TreeMap()
        assert self.tree.insert(3, 3).inorder_traversal() == [3]
        assert self.tree.insert(2, 2).inorder_traversal() == [2, 3]
        assert self.tree.insert(1, 1).inorder_traversal() == [1, 2, 3]

    def test_remove(self):
        self.tree = TreeMap()
        assert self.tree.remove(1) is None

        self.tree.insert(key=3, val=300).insert(key=1, val=100).insert(key=2, val=200)
        assert self.tree.remove(2).inorder_traversal() == [100, 300]
        assert self.tree.remove(1).inorder_traversal() == [300]
        assert self.tree.remove(3) is None

        self.tree.insert(key=3, val=300).insert(key=1, val=100).insert(6, 100).insert(7, 700)
        assert self.tree.remove(6).inorder_traversal() == [100, 300, 700]

    def test_remove_with_two_children(self):
        self.tree = TreeMap()
        (self.tree
         .insert(key=5, val=500)
         .insert(key=3, val=300)
         .insert(key=7, val=700)
         .insert(key=6, val=600)
         .insert(key=8, val=800))

        result = self.tree.remove(7).inorder_traversal()
        assert result == [300, 500, 600, 800]
