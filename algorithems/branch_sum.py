# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    sums = []
    cal_sum(root, 0, sums)
    return sums
    
def cal_sum(node, current, sums):
    if(node == None):
        return
        
    new_current = current + node.value
    if node.left == None and node.right == None:
        sums.append(new_current)
        return
        
    cal_sum(node.left, new_current, sums)
    cal_sum(node.right, new_current, sums)
