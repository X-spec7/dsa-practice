"""
Variant of Min Cost Climbing Stairs that also returns the steps taken.

After computing dp, backtrack from the last step to reconstruct which
steps were actually used to achieve the minimum cost.
"""

class Solution:
    def minCostClimbingStairs(self, costs: list[int]) -> tuple[int, list[int]]:
        n = len(costs)

        if n == 1:
            return costs[0], [0]

        dp = [0] * n
        dp[0] = costs[0]
        dp[1] = costs[1]

        for i in range(2, n):
            dp[i] = costs[i] + min(dp[i-1], dp[i-2])

        # Start backtracking from whichever of the last two steps was cheaper
        steps = []
        i = n - 1 if dp[n-1] < dp[n-2] else n - 2

        while i >= 0:
            steps.append(i)
            if i < 2:
                break
            i = i - 1 if dp[i-1] <= dp[i-2] else i - 2

        steps.reverse()
        return min(dp[n-1], dp[n-2]), steps


while True:
    try:
        costs = list(map(int, input("Input cost array, separated by spaces: ").split()))
        if not costs:
            print("Cost array cannot be empty.")
            continue
        break
    except ValueError:
        print("Please input valid array of numbers.")

sol = Solution()
min_cost, steps = sol.minCostClimbingStairs(costs)

print("Steps taken:", " -> ".join(f"step {s} (cost {costs[s]})" for s in steps))
print("Minimum cost:", min_cost)
