class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        n = intLength//2
        output = []
        num = int("1" + "0" * (n-1))
        even = intLength%2 
        if even and len(str(num)) != intLength:
                num = num *10

        for q in queries:
            num_reverse = ''
            n_num = num + q-1
            for i in range(len(str(n_num))-1-even, -1, -1):
                num_reverse += (str(n_num)[i])
            pal = str(n_num) +  num_reverse
            if len(pal) > intLength:
                output.append(-1) 
            else:
                output.append(int(pal))
        return output