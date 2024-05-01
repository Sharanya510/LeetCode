class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def minimum_cost(i):
            if i <= 1:
                return 0
            if i in memo:
                return memo[i]

            down_one = cost[i - 1] + minimum_cost(i - 1)
            down_two = cost[i - 2] + minimum_cost(i - 2)
            memo[i] = min(down_one, down_two)
            return memo[i]

        memo = {}
        return minimum_cost(len(cost))
        
        
        # APPROACH -- BOTTOM UP -- ITERATIVE
        # minimum_cost = [0] * (len(cost) + 1)
        # for i in range(2, len(cost) + 1):
        #     take_one_step = minimum_cost[i - 1] + cost[i - 1]
        #     take_two_steps = minimum_cost[i - 2] + cost[i - 2]
        #     minimum_cost[i] = min(take_one_step, take_two_steps)
        # return minimum_cost[-1]
        

# [10, 15, 20]
# MIN_COST = [0, 0, 0, 0]

# i = 2, 3
# one_step = min_cost[1] + cost[1] = 0 + 15
# two_step = min_cost[0] + cost[0] = 0 + 10
# min_cost[2] = 10

# i = 3
# one_step = min_cost[2] + cost[2] = 10 + 20 = 30
# two_step = min_cost[1] + cost[1] = 0 + 15 = 15
# min_cost[2] = 15

