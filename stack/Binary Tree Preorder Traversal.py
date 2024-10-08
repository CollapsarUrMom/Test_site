from queue import LifoQueue

que = LifoQueue()


print('==========================================================')

class TreeNode(object):

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []

        while not que.empty() or root:

            while root:
                result.append(root.val)
                que.put(root)
                root = root.left
            root = que.get()
            root = root.right

        return result


root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.right.left = TreeNode(6)
root.left.right.right = TreeNode(7)
root.right = TreeNode(3)
root.right.right = TreeNode(8)
root.right.right.left = TreeNode(9)

tree = Solution()

print(tree.preorderTraversal(root))

