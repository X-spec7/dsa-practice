def uniquePathObstacle(m: int, n: int, grid: list[list[int]]):
    dp = [[1 - grid[r][c] for c in range(n)] for r in range(m)]
    
    for row in range(1, m):
        for col in range(1, n):
            if grid[row][col] != 1:
                dp[row][col] = dp[row - 1][col] + dp[row][col - 1]
    
    return dp[m - 1][n - 1]

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
            
pathCount = uniquePathObstacle(m, n, grid)

print("The possible path count is: ", pathCount)
