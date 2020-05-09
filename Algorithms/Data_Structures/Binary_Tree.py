# Made by Anirudh Lakra
# Binary Tree


class Tree:

    def __init__(self, root=None):

        self.root = root


    def set_root(self, root_val):

        root = Node(root_val)
        left = self.root.get_left()
        right = self.root.get_right()

        # Update root left/right branches.
        self.root = root
        self.root.set_left(left)
        self.root.set_right(right)


    def add(self, value):

        if self.root is None:
            node = Node(value)
            self.root = node
        else:
            self.add_helper(self.root, value)


    # Recursive auxiliary method to help put value in sorted
    # order.
    def add_helper(self, cur_node, value):

        if cur_node is None:
            node = Node(value)
            cur_node = node
        else:
            if cur_node.get_value() < value:
                if cur_node.get_right() is None:
                    node = Node(value)
                    cur_node.set_right(node)
                else:
                    self.add_helper(cur_node.get_right(), value)
            else:
                if cur_node.get_left() is None:
                    node = Node(value)
                    cur_node.set_left(node)
                else:
                    self.add_helper(cur_node.get_left(), value)


    def print(self):

        self.print_helper(self.root.get_left())
        print(self.root.get_value())
        self.print_helper(self.root.get_right())


    # Recursive auxiliary method to help print tree in order from
    # smallest to biggest.
    def print_helper(self, cur_node):

        if cur_node.get_left():
            self.print_helper(cur_node.get_left())
        print(cur_node.get_value())
        if cur_node.get_right():
            self.print_helper(cur_node.get_right())


# Class for elements of tree.
class Node:

    def __init__(self, value=None, left=None, right=None):

        self.value = value
        self.left = left
        self.right = right


    def get_value(self):

        return self.value


    def get_left(self):

        return self.left


    def get_right(self):

        return self.right


    def set_left(self, node):

        self.left = node


    def set_right(self, node):

        self.right = node
    

def test_binary_tree():

    root = Node(50)
    tree = Tree(root)
    tree.add(30)
    tree.add(20)
    tree.add(80)
    tree.add(90)
    tree.add(3)
    tree.print()

test_binary_tree()
