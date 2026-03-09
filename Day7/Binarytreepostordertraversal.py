class Solution(object):
    def postorderTraversal(self, root):
       result =[]
       self.postorder(root,result)
       return result
    def postorder(self,root,result):
        if(root==None):
            return
        self.postorder(root.left,result)
        self.postorder(root.right,result)
        result.append(root.val)