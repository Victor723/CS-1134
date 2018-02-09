import LinkedBinaryTree

l_ch1 = LinkedBinaryTree.LinkedBinaryTree.Node(5)
r_ch1 = LinkedBinaryTree.LinkedBinaryTree.Node(1)
l_ch2 = LinkedBinaryTree.LinkedBinaryTree.Node(9, l_ch1, r_ch1)
l_ch3 = LinkedBinaryTree.LinkedBinaryTree.Node(2,l_ch2)
l_ch4 = LinkedBinaryTree.LinkedBinaryTree.Node(8)
r_ch2 = LinkedBinaryTree.LinkedBinaryTree.Node(4)
r_ch3 = LinkedBinaryTree.LinkedBinaryTree.Node(7, l_ch4, r_ch2)
root = LinkedBinaryTree.LinkedBinaryTree.Node(3, l_ch3, r_ch3)
tree = LinkedBinaryTree.LinkedBinaryTree(root)
x = tree.height()
print(x)
L= tree.leaves_list()
print(L)
def min_and_max(bin_tree):
        return subtree_min_and_max(bin_tree,bin_tree.root)
def subtree_min_and_max(bin_tree,subtree_root):
    if subtree_root.left is None and subtree_root.right is None:
        return (subtree_root.data,subtree_root.data)
    elif subtree_root.left is None:
        return (min(subtree_root.data,subtree_min_and_max(bin_tree,subtree_root.right)[0]),
                max(subtree_root.data,subtree_min_and_max(bin_tree,subtree_root.right)[1]))
    elif subtree_root.right is None:
        return (min(subtree_root.data,subtree_min_and_max(bin_tree,subtree_root.left)[0]),
                max(subtree_root.data,subtree_min_and_max(bin_tree,subtree_root.left)[1]))
    else:
        return (min(subtree_root.data, subtree_min_and_max(bin_tree,subtree_root.left)[0],
                subtree_min_and_max(bin_tree,subtree_root.right)[0]),
                max(subtree_root.data,subtree_min_and_max(bin_tree,subtree_root.left)[1],
                subtree_min_and_max(bin_tree,subtree_root.right)[1]))
print(min_and_max(tree))
def is_height_balanced(bin_tree):
    return helper(bin_tree.root)
def helper(root):
    if root.right is None and root.left is None:
        return True
    elif root.left is None:
        if root.subtree_height(root.right)==1:return helper(root.right)
        else:return False
    elif root.right is None:
        if root.subtree_height(root.left)==1:return helper(root.left)
        else:return False
    else:
        if abs(root.subtree_height(root.left)-root.subtree_height(root.right))<=1:
            return helper(root.left)+helper(root.right)
        else:
            return False
print(is_height_balanced(tree))