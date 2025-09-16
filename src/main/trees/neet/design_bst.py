class Tree:
    def __init__(self, key, val):
        self.right = None
        self.key = key
        self.val = val
        self.left = None


class TreeMap:
    def __init__(self):
        self.root = None

    def insert(self, key, val):
        new_node = Tree(key, val)
        if not self.root:
            self.root = new_node
            return self

        ptr = self.root
        while True:
            if key > ptr.key:
                if not ptr.right:
                    ptr.right = new_node
                    return self
                ptr = ptr.right
            elif key < ptr.key:
                if not ptr.left:
                    ptr.left = new_node
                    return self
                ptr = ptr.left
            else:
                ptr.val = val
                return self

    def get(self, key):
        if self.root:
            ptr = self.root
            while True:
                if key > ptr.key:
                    ptr = ptr.right
                elif key < ptr.key:
                    ptr = ptr.left
                else:
                    return ptr.val
        return -1

    def get_min(self):
        node = self.find_min(self.root)
        return node.val if node else -1

    def get_max(self):
        ptr = self.root
        while ptr and ptr.right:
            ptr = ptr.right
        return ptr.val if ptr else -1

    def inorder_traversal(self):
        result = []

        def inorder(node):
            if node:
                inorder(node.left)
                result.append(node.val)
                inorder(node.right)

        inorder(self.root)
        return result

    def remove(self, key):
        self.root = self.remove_it(self.root, key)

    def remove_it(self, node, key):
        if not node:
            return
        if key > node.key:
            node.right = self.remove_it(node.right, key)
        elif key < node.key:
            node.left = self.remove_it(node.left, key)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            min_node = self.find_min(node.right)
            node.val = min_node.val
            node.key = min_node.key
            node.right = self.remove_it(node.right, node.key)
        return node

    @staticmethod
    def find_min(node):
        ptr = node
        while ptr and ptr.left:
            ptr = ptr.left
        return ptr if ptr else None
