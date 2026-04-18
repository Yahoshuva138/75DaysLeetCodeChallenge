class Solution(object):
    def isSubtree(self, root, subRoot):
        
        # helper: check if two trees are identical
        def isSame(a, b):
            if not a and not b:
                return True
            if not a or not b:
                return False
            return (a.val == b.val and
                    isSame(a.left, b.left) and
                    isSame(a.right, b.right))
        
        # main logic
        if not root:
            return False
        
        # check current node OR recurse left/right
        return (isSame(root, subRoot) or
                self.isSubtree(root.left, subRoot) or
                self.isSubtree(root.right, subRoot))