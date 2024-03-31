class Solution:
    def pathSum(self, nums: List[int]) -> int:
        dic ={}
        for num in nums: 
            depth= num//100
            position = num%100//10
            value = num%100%10
            dic[(depth,position)] = value
        root = (nums[0]//100,nums[0]%100//10)
        stack =[(root,0)]
        ans = 0
       # the postion of left node for a node should be (row+1,2*col-1) and 
       # the right node should be (row+1,2*col) since the descpriton explains that
       # its position should be as same as in the full binary tree
       #conduct dfs search 
        while stack:
            node,curr = stack.pop()
            depth,position = node
            if (depth+1, 2*position-1) not in dic.keys() and (depth+1, 2*position) not in dic.keys():
                ans += curr+dic[node]
            curr += dic[node]
            if (depth+1, 2*position-1) in dic.keys():
                stack.append(((depth+1, 2*position-1),curr))
            if (depth+1, 2*position) in dic.keys():
                stack.append(((depth+1, 2*position),curr))

        return ans
