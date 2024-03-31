class Solution:
    def pathSum(self, nums: List[int]) -> int:
        dic ={}
        for num in nums: 
            depth= num//100
            position = num// 10 % 10
            value = num % 10
            dic[(depth,position)] = value
        root = (nums[0]//100,nums[0]// 10 % 10)
        stack =[(root,0)]
        ans = 0
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
