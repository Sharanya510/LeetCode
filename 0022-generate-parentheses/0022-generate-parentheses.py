class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        curr_string = ""
        opencount, closedcount = 0, 0
        self.backtrack(res, curr_string, opencount, closedcount, n)
        return res
    
    def backtrack(self,res, curr_string, opencount, closedcount, n):
        if len(curr_string) == 2 * n:
            res.append(curr_string)
            return 
        
        if (opencount < n):
            # curr_string += "("
            self.backtrack(res, curr_string + "(", opencount + 1, closedcount, n)
            # curr_string -= "("
            
        if (opencount > closedcount):
            # curr_string += ")"
            self.backtrack(res, curr_string + ")", opencount, closedcount+1, n)
            # curr_string -= ")"
        
        