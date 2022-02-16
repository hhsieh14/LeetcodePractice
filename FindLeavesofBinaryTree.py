class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        def DFS(node, mylist):  
            level = 0
            if node.left != None:
                DFS(node.left, mylist)
                level = max(level, 1 + node.left.val[0])
            
            if node.right != None:
                DFS(node.right, mylist)
                level = max(level, 1 + node.right.val[0])
            
           
            node.val = (level, node.val)
            if level in mylist:
                mylist[level].append(node.val[-1])
            else:
                mylist[level] = [node.val[-1], ]
            return mylist
        
        table = {}
        DFS(root, table)
        output = []
        for key in table.keys():
            output.append(table[key])
        return output
