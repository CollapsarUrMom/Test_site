from queue import LifoQueue
print('==========================================================')

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(8)
root.left.right.left = TreeNode(6)
root.left.right.right = TreeNode(7)
root.right.right.left = TreeNode(9)


que = LifoQueue()
result = []

while not que.empty() or root:

    while root:
        que.put(root)
        root = root.left
    root = que.get()
    result.append(root.val)
    root = root.right


print(result)
    

    


# [4,2,6,5,7,1,3,9,8]