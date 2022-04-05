class NotFound(Exception):
    pass

class BinaryNode:
    def __init__(self, data = None, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self):
        self.root = None

    def add_recur(self, node, value): #O(log2(n))
        if node == None:
            return BinaryNode(value)
        elif value > node.data:
            node.right = self.add_recur(node.right, value)
        elif value < node.data:
            node.left = self.add_recur(node.left, value)
        return node

    def add(self, value:int):
        """"""
        if self.root == None:
            self.root = BinaryNode(value)
        else:
            self.add_recur(self.root, value)

    def find_recur(self, node, value):
        if node == None:
            return
        elif value > node.data:
            return self.find_recur(node.right, value)
        elif value < node.data:
            return self.find_recur(node.left, value)
        return node

    def find(self, value): #O(log2(n))
        """"""
        ret_node = self.find_recur(self.root, value)
        if ret_node:
            return ret_node.data
        raise NotFound()
    
    def _postorder_recur(self, node):
        """
        What is postorder?
        1. We got all the way to the left from the root and print the left-most node
        2. once we hit None, we return from the left and try to go right and print the right-most node
        3. on the way back from the right, we print out our nodes
        4. then we go to the right and try to go left from the root.right node and print the left-most node
        5. once we hit None, we return and print on the way back, making the root the last print
        """
        if node == None:
            return
        self._postorder_recur(node.left)
        self._postorder_recur(node.right)
        print(node.data, end=" ")

    def print_postorder(self):
        self._postorder_recur(self.root)

    def _preorder_recur(self, node):
        """
        What is preorder?
        1. Prints the root first
        2. Prints to the left as far as possible, each node is printed along the way
        3. returns to a node that has a right node, and prints the right, each node printed along the way
        4. returns to the root, prints to the right from the root, if there are nodes to the left, we print left first
            and right second.    
        """
        if node == None:
            return
        print(node.data, end=" ")
        self._preorder_recur(node.left)
        self._preorder_recur(node.right)

    def print_preorder(self):
        self._preorder_recur(self.root)


    def _inorder_recur(self, node):
        """
        What is inorder?
        Very similar to the postorder, except instead of printing left-most to right-most,
        we simply go left-most and print the return nodes on the way back and then return to right-most
        """
        if node == None:
            return
        self._inorder_recur(node.left)
        print(node.data, end=" ")
        self._inorder_recur(node.right)

    def print_inorder(self):
        self._inorder_recur(self.root)
    
    def _sum_recur(self, node):
        if node == None:
            return 0
        return node.data + self._sum_recur(node.left) + self._sum_recur(node.right)
    
    def tree_sum(self):
        """A function that calculates the sum of the whole tree"""
        return self._sum_recur(self.root)

    def remove_subtree(self, data):
        self.root = self.remove_subtree_recur(self.root, data)

    def remove_subtree_recur(self, node, data):
        if node == None:
            return None
        elif data < node.data:
            node.left = self.remove_subtree_recur(node.left, data)
        elif node.data < data:
            node.right = self.remove_subtree_recur(node.right, data)
        else:
            # subtree_size = self.subtree_count(node)
            # self.size -= subtree_size
            return None
        return node

    def subtree_count(self, node):
        """Má henda þessum með ef þarf"""
        if node == None:
            return 0
        return 1 + self.subtree_count(node.left) + self.subtree_count(node.right)


if __name__ == '__main__':
    bt = BinaryTree()
    bt.add(5)
    bt.add(9)
    bt.add(3)
    bt.add(4)
    bt.add(11)
    bt.add(6)
    bt.add(1)
    print("Node found: ",bt.find(11))
    bt.print_preorder()  # 5 3 1 4 9 6 11
    print()
    bt.print_postorder() # 1 4 3 6 11 9 5
    print()
    bt.print_inorder()   # 1 3 4 5 6 9 11
    print()
    print(bt.tree_sum())
    bt.remove_subtree(9)
    bt.print_preorder()