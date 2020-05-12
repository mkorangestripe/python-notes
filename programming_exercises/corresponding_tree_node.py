# Find the corresponding node of a binary tree in a cloned tree.
# Given two binary trees (original and cloned) and a reference to a node target in the original tree...
# return a reference to the same node in the cloned tree.

# Definition for the binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# target = 3
# tree = [7,4,3,null,null,6,19]
treenode1 = TreeNode(7)
treenode1.left = TreeNode(4)
treenode1.right = TreeNode(3)
treenode1.right.left = 6
treenode1.right.right = 19

treenode_clone1 = treenode1
target1 = treenode1.right


# target = 13
# [23,9,29,null,28,27,19,null,null,null,null,13,1,null,null,26,25,6]
#                         23
#             9                           29
#      null       28             27                 19
#             null null      null null      13               1
#                                       null null      26         25
#                                                    6 null    null null
treenode2 = TreeNode(23)
treenode2.left = TreeNode(9)
treenode2.right = TreeNode(29)
treenode2.left.right = TreeNode(28)
treenode2.right.left = TreeNode(27)
treenode2.right.right = TreeNode(19)
treenode2.right.right.left = TreeNode(13)
treenode2.right.right.right = TreeNode(1)
treenode2.right.right.right.left = TreeNode(26)
treenode2.right.right.right.right = TreeNode(25)
treenode2.right.right.right.left.left = 6

treenode_clone2 = treenode2
target2 = treenode2.right.right.left


class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:

        if original is None:
            return original

        if original is target:
            return cloned

        left = self.getTargetCopy(original.left, cloned.left, target)

        if left is not None:
            return left

        return self.getTargetCopy(original.right, cloned.right, target)


solution = Solution()
target_clone1 = solution.getTargetCopy(treenode1, treenode_clone1, target1)
target_clone2 = solution.getTargetCopy(treenode2, treenode_clone2, target2)
print(target_clone1.val)  # 3
print(target_clone2.val)  # 13
# Runtime: 644 ms
# Memory Usage: 23.4 MB
