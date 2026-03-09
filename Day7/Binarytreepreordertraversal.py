class Solution(object):
    def preorderTraversal(self, root):
       result =[]
       self.preorder(root,result)
       return result
    def preorder(self,root,result):
        if(root==None):
            return
        result.append(root.val)
        self.preorder(root.left,result)
        self.preorder(root.right,result)