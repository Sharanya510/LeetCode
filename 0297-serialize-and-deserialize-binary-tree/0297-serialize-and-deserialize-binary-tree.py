# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def __init__(self):
        self.res=""
        
    def serialize(self, root):
        if root is None:
            self.res+="None,"
        else: 
            self.res+=str(root.val)+','
            self.serialize(root.left)
            self.serialize(root.right)
        # print(self.res)
        return self.res
        

    def deserialize(self, data):
        def helper(data_list):
            node=data_list.pop(0)
            if node=='None':
                return None
            root=TreeNode(int(node))
            root.left=helper(data_list)
            root.right=helper(data_list)
            
            return root
                
        
        data_list=data.split(',')
        return helper(data_list)
        
# 1,2,None,None,3,4,None,None,5,None,None,



# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))