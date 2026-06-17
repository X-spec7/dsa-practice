def uniquePathObstacle(m: int, n: int, grid: list[list[int]]):
    dp = [[1 - grid[r][c] for c in range(n)] for r in range(m)]

    for c in range(1, n):
        dp[0][c] = 0 if grid[0][c] == 1 else dp[0][c - 1]

    for r in range(1, m):
        dp[r][0] = 0 if grid[r][0] == 1 else dp[r - 1][0]

    for row in range(1, m):
        for col in range(1, n):
            if grid[row][col] != 1:
                dp[row][col] = dp[row - 1][col] + dp[row][col - 1]
    
    return dp[m - 1][n - 1]


def uniquePathObstacleOptimized(m: int, n: int, grid: list[list[int]]) -> int:
    if grid[0][0] == 1 or grid[m-1][n-1] == 1:
        return 0

    dp = [0] * n
    dp[0] = 1

    for c in range(1, n):
        dp[c] = 0 if grid[0][c] == 1 else dp[c - 1]

    for r in range(1, m):
        dp[0] = 0 if grid[r][0] == 1 else dp[0]
        for c in range(1, n):
            if grid[r][c] == 1:
                dp[c] = 0
            else:
                dp[c] += dp[c - 1]

    return dp[n - 1]


while True:
    try:
        m, n = map(int, input("Enter the grid size (rows, cols): ").split())
        
        if m <= 0 or n <= 0:
            print("Grid size should be positive number.")
            continue
        
        break
    except ValueError:
        print("Please input valid grid size parameters.")
        
grid = []

for i in range(m):
    while True:
        try:
            row = list(map(int, input(f"Input the {i+1}th row: ").split()))
            
            if len(row) != n:
                print(f"The length of each row should be {n}")
                continue

            if any(v != 0 and v != 1 for v in row):
                print("All values in a row should be 0 or 1.")
                continue

            grid.append(row)
            break
        except ValueError:
            print("Please input valid row of 0 and 1.")
            
print("2D dp:        ", uniquePathObstacle(m, n, grid))
print("Optimized dp: ", uniquePathObstacleOptimized(m, n, grid))
