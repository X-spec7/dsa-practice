class Solution:
    def minimumPathSum(self, m: int, n: int, grid: list[list[int]]) -> input:
        dp = [[0] * n for _ in range(m)]
        
        for row in range(m):
            for column in range(n):
                dp[row][column] = min(dp[row][column - 1], dp[row - 1][column]) + grid[row][column]
        
        return dp[m - 1][n - 1]

while True:
    try:
        m, n = map(int, input("Enter grid size (rows cols): ").split())
        if m <= 0 or n <= 0:
            print("Rows and cols must be positive integers.")
            continue
        break
    except ValueError:
        print("Invalid input. Enter two integers separated by a space.")

grid = []
print(f"Enter {m} rows, each with {n} non-negative integers separated by spaces:")
for i in range(m):
    while True:
        try:
            row = list(map(int, input(f"  Row {i+1}: ").split()))
            if len(row) != n:
                print(f"Expected {n} values, got {len(row)}. Try again.")
                continue
            if any(v < 0 for v in row):
                print("All values must be non-negative. Try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Enter integers only.")
    grid.append(row)

print("Grid accepted:", grid)

sol = Solution()

minimumPathSum = sol.minimumPathSum(m, n, grid)

print("The minimum path sum is: ", minimumPathSum)
