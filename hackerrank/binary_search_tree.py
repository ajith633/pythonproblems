class Queue:
    def __init__(self):
        self.items=[]
    def enqueue(self,item):
        self.items.append(item)
    def dequeue(self):
        return(self.items.pop(0))
    def peek(self):
        return(self.items[0])
    def is_empty(self):
        return(len(self.items)==0)

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

    def print_tree(self, order="in"):
        if(self.root!=None):
            str_out=""
            if(order == "in"):
                print("In-order: "+self._in_order_print_tree(self.root,str_out))
            elif(order == "pre"):
                print("Pre-order: "+self._pre_order_print_tree(self.root,str_out))
            elif(order == "post"):
                print("Post-order: "+self._post_order_print_tree(self.root,str_out))
            elif (order == "level"):
                print("Level-order: "+self._level_order_print_tree(self.root, str_out))
            else:
                print("Invalid print order")

    def _in_order_print_tree(self,curr_node,str_out):
        if(curr_node is not None):
            str_out=self._in_order_print_tree(curr_node.left_child,str_out)
            str_out += str(curr_node.value) + "-"
            str_out=self._in_order_print_tree(curr_node.right_child,str_out)
        return(str_out)
    def _pre_order_print_tree(self,curr_node,str_out):
        if(curr_node is not None):
            str_out += str(curr_node.value) + "-"
            str_out=self._pre_order_print_tree(curr_node.left_child,str_out)
            str_out=self._pre_order_print_tree(curr_node.right_child,str_out)
        return(str_out)
    def _post_order_print_tree(self,curr_node,str_out):
        if(curr_node is not None):
            str_out=self._post_order_print_tree(curr_node.left_child,str_out)
            str_out=self._post_order_print_tree(curr_node.right_child,str_out)
            str_out += str(curr_node.value) + "-"
        return(str_out)
    def _level_order_print_tree(self,curr_node,str_out):
        if(curr_node is not None):
            q=Queue()
            q.enqueue(curr_node)
            while(not q.is_empty()):
                node=q.dequeue()
                str_out+=str(node.value)+"-"
                if(node.left_child):
                    q.enqueue(node.left_child)
                if(node.right_child):
                    q.enqueue(node.right_child)
        return(str_out)
    def _level_order_print_tree2(self, curr_node, str_out):
        if (curr_node is not None):
            items=[]
            items.append(curr_node)
            while (len(items)>0):
                node = items.pop(0)
                str_out += str(node.value) + "-"
                if (node.left_child):
                    items.append(node.left_child)
                if (node.right_child):
                    items.append(node.right_child)
        return (str_out)
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

if __name__ == "__main__":
    b=BinarySearchTree()
    arr=[7, 3, 5, 2, 1, 4, 6, 7]
    from random import randint
    #for _ in range(20):
    #    b.insert(randint(0,100))
    for i in arr:
        b.insert(i)
    b.print_tree("in")
    b.print_tree("pre")
    b.print_tree("post")
    b.print_tree("level")
    print("Height is :",b.height())
    print("Total elements are:",b.count())
    print("Search for 51:",b.search(51))

