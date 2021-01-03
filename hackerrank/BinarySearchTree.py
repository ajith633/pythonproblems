

class Node:
    def __init__(self, value=None):
        self.value=value
        self.right_child=None
        self.left_child=None


class BinarySearchTree:
    def __init__(self):
        self.root=None

    def insert(self, value):
        print("inserting",value)
        if(self.root==None):
            self.root=Node(value)
        else:
            self._insert(value,self.root)

    def _insert(self,value,curr_node):

        if(value < curr_node.value):
            if(curr_node.left_child==None):
                curr_node.left_child=Node(value)
            else:
                self._insert(value,curr_node.left_child)
        elif(value > curr_node.value):
            if(curr_node.right_child==None):
                curr_node.right_child=Node(value)
            else:
                self._insert(value,curr_node.right_child)
        else:
            print("Duplication insertion attempted, skipping value {}".format(value))

    def print_tree(self):
        if(self.root!=None):
            self._print_tree(self.root)

    def _print_tree(self,curr_node):
        if(curr_node==None):
            return
        self._print_tree(curr_node.left_child)
        print(curr_node.value)
        self._print_tree(curr_node.right_child)

    def height(self):
        return(self._height(self.root,0))

    def _height(self,curr_node,curr_height):
        if(curr_node==None): return(curr_height)
        curr_height+=1
        left_height=self._height(curr_node.left_child,curr_height)
        right_height=self._height(curr_node.right_child,curr_height)
        return(max(left_height,right_height))

    def search(self,value):
        if(self.root==None):
            return(False)
        else:
            return(self._search(value,self.root))

    def _search(self,value,curr_node):
        if(curr_node==None): return(False)
        if(value==curr_node.value): return(True)
        elif(value<curr_node.value):
            return(self._search(value,curr_node.left_child))
        else:
            return (self._search(value,curr_node.right_child))

    def count(self):
        return(self._count(self.root))

    def _count(self,curr_node):
        if(curr_node==None):
            return(0)
        else:
            return(1+self._count(curr_node.left_child)+self._count(curr_node.right_child))


b=BinarySearchTree()
from random import randint
for _ in range(20):
    b.insert(randint(0,100))

b.print_tree()
print("Height is :",b.height())
print("Total elements are:",b.count())
print("Search for 51:",b.search(51))

