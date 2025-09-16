from trees.neet.design_bst import TreeMap


class TestDesignBst:
    def test_root_is_none_when_tree_initialized(self):
        tree = TreeMap()
        assert not tree.root

    def test_insert_sets_root_when_tree_empty(self):
        tree = TreeMap().insert(key=1, val=100)
        assert tree.root.key == 1
        assert tree.root.val == 100

    def test_insert_places_node_on_right_when_key_greater(self):
        tree = TreeMap().insert(key=1, val=100).insert(key=2, val=200)
        assert tree.root.right.key == 2
        assert tree.root.right.val == 200

    def test_insert_places_node_on_left_when_key_smaller(self):
        tree = TreeMap().insert(key=3, val=300).insert(key=2, val=200)
        assert tree.root.left.key == 2
        assert tree.root.left.val == 200

    def test_insert_overwrites_value_when_key_exists(self):
        tree = TreeMap().insert(key=1, val=10).insert(key=1, val=100)
        assert tree.root.key == 1
        assert tree.root.val == 100

    def test_get_returns_negative_one_when_tree_empty(self):
        tree = TreeMap()
        assert tree.get(1) == -1

    def test_get_returns_value_for_existing_keys(self):
        tree = TreeMap()
        tree.insert(key=3, val=300).insert(key=1, val=100).insert(key=2, val=200)
        assert tree.get(1) == 100
        assert tree.get(2) == 200
        assert tree.get(3) == 300

    def test_get_min_returns_negative_one_when_tree_empty(self):
        tree = TreeMap()
        assert tree.get_min() == -1

    def test_get_min_returns_smallest_key_value(self):
        tree = TreeMap()
        tree.insert(key=2, val=2).insert(key=11, val=11).insert(key=31, val=31)
        assert tree.get_min() == 2

    def test_get_max_returns_negative_one_when_tree_empty(self):
        tree = TreeMap()
        assert tree.get_max() == -1

    def test_get_max_returns_largest_key_value(self):
        tree = TreeMap()
        tree.insert(key=2, val=2).insert(key=11, val=11).insert(key=31, val=31)
        assert tree.get_max() == 31

    def test_inorder_traversal_returns_sorted_values(self):
        tree = TreeMap()
        assert tree.insert(3, 3).inorder_traversal() == [3]
        assert tree.insert(2, 2).inorder_traversal() == [2, 3]
        assert tree.insert(1, 1).inorder_traversal() == [1, 2, 3]

    def test_remove_returns_none_when_tree_empty(self):
        tree = TreeMap()
        assert tree.remove(1) is None

    def test_remove_leaf_node_updates_tree_correctly(self):
        tree = TreeMap()
        tree.insert(3, 300).insert(1, 100).insert(2, 200)
        assert tree.remove(2).inorder_traversal() == [100, 300]

    def test_remove_node_with_only_left_child_updates_tree_correctly(self):
        tree = TreeMap()
        tree.insert(3, 300).insert(1, 100)
        assert tree.remove(1).inorder_traversal() == [300]

    def test_remove_node_with_only_right_child_updates_tree_correctly(self):
        tree = TreeMap()
        tree.insert(3, 300).insert(6, 100).insert(7, 700)
        assert tree.remove(6).inorder_traversal() == [300, 700]

    def test_remove_root_node_returns_none_when_single_node(self):
        tree = TreeMap()
        tree.insert(3, 300)
        assert tree.remove(3) is None

    def test_remove_node_with_two_children_replaces_with_inorder_successor(self):
        tree = TreeMap()
        (tree
         .insert(key=5, val=500)
         .insert(key=3, val=300)
         .insert(key=7, val=700)
         .insert(key=6, val=600)
         .insert(key=8, val=800))

        result = tree.remove(7).inorder_traversal()
        assert result == [300, 500, 600, 800]
