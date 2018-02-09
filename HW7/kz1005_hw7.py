class EmptyCollection(Exception):
    pass
class EmptyTree(Exception):
    pass

class LinkedBinaryTree:
    class Node:
        def __init__(self, data, left=None, right=None):
            self.data = data
            self.left = left
            if (self.left is not None):
                self.left.parent = self
            self.right = right
            if (self.right is not None):
                self.right.parent = self
            self.parent = None

    def __init__(self, root=None):
        self.root = root
        self.size = self.subtree_count(self.root)

    def __len__(self):
        return self.size

    def is_empty(self):
        return (len(self) == 0)

    def subtree_count(self, subtree_root):
        if(subtree_root is None):
            return 0
        else:
            left_count = self.subtree_count(subtree_root.left)
            right_count = self.subtree_count(subtree_root.right)
            return left_count + right_count + 1


    def sum_tree(self):
        return self.subtree_sum(self.root)

    def subtree_sum(self, subtree_root):
        if(subtree_root is None):
            return 0
        else:
            left_sum = self.subtree_sum(subtree_root.left)
            right_sum = self.subtree_sum(subtree_root.right)
            return left_sum + right_sum + subtree_root.data

    def height(self):
        if (self.is_empty()):
            raise EmptyCollection("Height is not defined for an empty tree")
        return self.subtree_height(self.root)

    def subtree_height(self, subtree_root):
        if((subtree_root.left is None) and (subtree_root.right is None)):
            return 0
        elif(subtree_root.left is None):
            return 1 + self.subtree_height(subtree_root.right)
        elif(subtree_root.right is None):
            return 1 + self.subtree_height(subtree_root.left)
        else:
            left_height = self.subtree_height(subtree_root.left)
            right_height = self.subtree_height(subtree_root.right)
            return 1 + max(left_height, right_height)
    
    
    def iterative_inorder(self):
        current=self.root
        while current is not None:
            if current.left is None:
                yield current.data
                current=current.right
            else:
                pre=current.left
                while pre.right!=None and pre.right!=current:
                    pre=pre.right
                if pre.right is None:
                    pre.right=current
                    current=current.left
                else:
                    pre.right=None
                    yield current.data
                    current=current.right

# Question 2
    def leaves_list(self):
        answer=[]
        node=self.root
        if node is None:
            return answer
        def leaves(node):
            if node.left is None and node.right is None:
                answer.append(node.data)
            if node.left is not None:
                leaves(node.left)
            if node.right is not None:
                leaves(node.right)
        leaves(node)
        return answer


# Question 1
def min_and_max(bin_tree):
    if bin_tree.root is None:
        raise EmptyTree("tree is empty")
    return subtree_min_and_max(bin_tree,bin_tree.root)
def subtree_min_and_max(bin_tree,subtree_root):
    if subtree_root.left is None and subtree_root.right is None:
        return (subtree_root.data,subtree_root.data)
    e1=subtree_root.data
    if subtree_root.left is None:
        e2=subtree_min_and_max(bin_tree,subtree_root.right)
        return (min(e1,e2[0]),max(e1,e2[1]))
    elif subtree_root.right is None:
        e3=subtree_min_and_max(bin_tree,subtree_root.left)
        return (min(e1,e3[0]),max(e1,e3[1]))
    else:
        e2=subtree_min_and_max(bin_tree,subtree_root.right)
        e3=subtree_min_and_max(bin_tree,subtree_root.left)
        return (min(e1, e3[0],e2[0]),max(e1,e3[1],e2[1]))
#Question 3
def is_height_balanced(bin_tree):
    return helper(bin_tree.root)[1]
def helper(root):
    if root == None:
        return (0,True)
    else:
        root_left=helper(root.left)
        root_right=helper(root.right)
        balanced=root_left[1] and root_right[1] and abs(root_left[0]-root_right[1])<=1
        return (1+max(root_left[0],root_right[0]),balanced)

#Question 5
def create_expression_tree(prefix_exp_str):
    prefix=prefix_exp_str.split()
    L=['+','-','*','/']
    def helper(prefix,index):
        if prefix[index].isdigit():
            return (LinkedBinaryTree.Node(int(prefix[index])),index)
        elif prefix[index] in L:
            node = LinkedBinaryTree.Node(prefix[index])
            left=helper(prefix,index+1)
            node.left=left[0]
            right=helper(prefix,left[1]+1)
            node.right=right[0]
            return (node,right[1])
    return LinkedBinaryTree(helper(prefix,0)[0])

def prefix_to_postfix(prefix_exp_str):
    tree=create_expression_tree(prefix_exp_str)
    L=[]
    def helper(root):
        if isinstance(root.data,int):
            L.append(str(root.data))
        else:
            helper(root.left)
            helper(root.right)
            L.append(root.data)
    helper(tree.root)
    return ' '.join(L)

l_ch1 = LinkedBinaryTree.Node(5)
r_ch1 = LinkedBinaryTree.Node(1)
l_ch2 = LinkedBinaryTree.Node(9, l_ch1, r_ch1)
l_ch3 = LinkedBinaryTree.Node(2,l_ch2)
l_ch4 = LinkedBinaryTree.Node(8)
r_ch2 = LinkedBinaryTree.Node(4)
r_ch3 = LinkedBinaryTree.Node(7, l_ch4, r_ch2)
root = LinkedBinaryTree.Node(3, l_ch3, r_ch3)
tree = LinkedBinaryTree(root)
tree2=LinkedBinaryTree(l_ch2)
print(is_height_balanced(tree))
print(is_height_balanced(tree2))
print(min_and_max(tree))
l1=LinkedBinaryTree.Node(5)
l2=LinkedBinaryTree.Node(1)
l3=LinkedBinaryTree.Node(8,l1,l2)
l4=LinkedBinaryTree.Node(9)
l5=LinkedBinaryTree.Node(2,l4)
l6=LinkedBinaryTree.Node(4)
l7=LinkedBinaryTree.Node(7,l3,l6)
l8=LinkedBinaryTree.Node(3,l5,l7)
tree3=LinkedBinaryTree(l8)
print(is_height_balanced(tree3))
print(min_and_max(tree3))
l1=LinkedBinaryTree.Node(5)
l2=LinkedBinaryTree.Node(1)
l3=LinkedBinaryTree.Node(8)
l4=LinkedBinaryTree.Node(9,l1,l2)
l5=LinkedBinaryTree.Node(2,l4)
l6=LinkedBinaryTree.Node(4)
l7=LinkedBinaryTree.Node(7,l3,l6)
l8=LinkedBinaryTree.Node(3,l5,l7)
tree4=LinkedBinaryTree(l8)
print(is_height_balanced(tree4))
print(min_and_max(tree4))
for item in tree.iterative_inorder():
    print(item, end=' ')
print('')
print(prefix_to_postfix('* + - 2 15 6 4')) 


