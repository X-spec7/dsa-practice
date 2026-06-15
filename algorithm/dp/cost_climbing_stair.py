"""
Docstring for algorithm.dp.cost_climbing_stair

Given an integer array of costs where each element is the cost of a specific step on stairs
Return the minimum cost to reach the top of the floor.

Condition: Once paid the cost, can either climb one or two steps.
Note:
    Here, the top doesn't mean the last step, but we should pass the last step of the stair.
"""

class Solution:
    def minCostClimbingStairs(self, costs: list[int]) -> int:
        n = len(costs)
        
        if n == 1:
            return costs[0]
        
        dp = [0] * n
        
        dp[0] = costs[0]
        dp[1] = costs[1]
        
        for i in range(2, n):
            dp[i] = costs[i] + min(dp[i-1], dp[i-2])
            
        return min(dp[n-1], dp[n-2])

while True:
    try:
        costs = list(map(int, input("Input cost array, separated by spaces: ").split()))
        if not costs:
            print("Cost array cannot be empty.")
        break
    except ValueError:
        print("Please input valid array of numbers.")

sol = Solution()

minCost = sol.minCostClimbingStairs(costs)

print("Minimum cost: ", minCost)
