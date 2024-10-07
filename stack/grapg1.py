roots = [1,2,3]

class TreeNode(object):

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def recurs(root, l):
        if root is None:
             return None
        
        next_recurs = recurs(root.left, l)
        




root = TreeNode(1)
# root.left = TreeNode(null)
root.left = TreeNode(2)
root.left.left = TreeNode(3)



print(f'result {recurs(roots[-1], 3)}')