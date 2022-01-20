class Node:
    
    def __init__(self,value,left=None,right=None):
        
        self.value = value
        self.left = left
        
        self.right = right
        
class BinaryTree:
    
    def __init__(self):
        self.head = None
        self.message = None
        self.traversed = []
        self.found = None
        self.succesoor = None
     
    def insert_helper(self,nodes,value):
        if nodes.value == value:
            self.message = "alraedy exists"
            return "already exists"
            
        if  value < nodes.value:
            if nodes.left != None:
                self.insert_helper(nodes.left,value)
            else:
                nodes.left = Node(value)
               #self.head = nodes
                self.message = "added"
            
            #print("added left")
            return "added left"+str(value)
            
        
        if value > nodes.value:
            if nodes.right != None:
                self.insert_helper(nodes.right,value)
            else:
                nodes.right = Node(value)
                self.message = "added"
                #self.head = nodes
                #print("added right")
                return "added right "+str(value)
                
            

    def insert(self,val):
        if self.head == None:
            self.head = Node(val)
            return "added at root"
            
        else:
            return self.insert_helper(self.head,val)
            
            
            #return self.head

    def inorder_traverse_helper(self,node):
        if node != None:
            self.inorder_traverse_helper(node.left)
            self.traversed.append(node.value)
            self.inorder_traverse_helper(node.right)
        


    def preorder_traverse_helper(self,node):
        if node != None:
            self.traversed.append(node.value)
            self.preorder_traverse_helper(node.left)
            
            self.preorder_traverse_helper(node.right)  
        


    def postorder_traverse_helper(self,node):
        if node != None:
            
            self.postorder_traverse_helper(node.left)
            
            self.postorder_traverse_helper(node.right)
            self.traversed.append(node.value)  


    def in_order_traversal(self):

        if self.head == None:
            return None

        else:
            self.traversed = []
            self.inorder_traverse_helper(self.head)
            return self.traversed


    def pre_order_traversal(self):

        if self.head == None:
            return None

        else:
            self.traversed=[]
            self.preorder_traverse_helper(self.head)
            return self.traversed
        

    def post_order_traversal(self):

        if self.head == None:
            return None

        else:
            self.traversed = []
            self.postorder_traverse_helper(self.head)
            return self.traversed


    def succesor_detect(self,node):

        
        def detect_succesor(nodes,parent=None):


            if nodes.left == None:
                return {'succesor_node':nodes,'parent':parent}

            else:
                if nodes.left != None:
                    self.detect_succesor(nodes.left,nodes)

        succesoor=detect_succesor(node.right,node)

        return succesoor



    def delete_helper(self,value,node,parent=None):
        if value == node.value:
            self.found = "got the item "+str(value)

            if node.left == None and node.right == None:
                if parent.left == node:
                    parent.left = None

                elif parent.right == node:
                    parent.right = None

            elif node.left == None:
                if parent.left == node:
                    parent.left = node.right

                if parent.right ==  node:
                    parent.right = node.right


            elif node.right == None:
                if parent.left == node:
                    parent.left = node.left

                if parent.right ==  node:
                    parent.right = node.left


            elif node.left != None and node.right !=  None:
                succesor = succesor_detect(node)

                create_node = Node(value=succesor.succesor_node.value,left=node.left,right=node.right)



                if succesor.parent.left == succesor.succesor_node:
                    succesor.parent.left = succesor.succesor_node.right

                if succesor.parent.right == succesor.succesor_node:
                    succesor.parent.right = succesor.succesor_node.right

                if parent.left == node:

                    parent.left = create_node

                if parent.right == node:
                    parent.right = create_node





        else:
            if node.left != None:

                if value < node.value:
                    self.delete_helper(value,node.left,parent=node)


            if node.right != None:
                if value > node.value:
                    self.delete_helper(value,node.right,parent=node)



    def delete(self,value):
        if self.head != None:
            b=self.delete_helper(value,self.head)

            return b
            

        else:
            return "Sorry , root value is None"

    def search(self,value):

        curr = self.head
        if curr == None:
            return False
        else:

            while curr != None and curr.value != value :

                if value > curr.value:
                    curr = curr.right

                elif value < curr.value:
                    curr = curr.left

        if curr != None:
            return True

        else:
            return False

        

        
            
checking = BinaryTree()
checking.insert(1)
checking.insert(0)
checking.insert(-1)
checking.insert(-3)
checking.insert(2)
checking.insert(3)
checking.insert(4)
checking.insert(5)
checking.insert(6)
checking.insert(7)



print(checking.in_order_traversal())

checking.delete(7)

print(checking.in_order_traversal())

print(checking.search(6))




            
            