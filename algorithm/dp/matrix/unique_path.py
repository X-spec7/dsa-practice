def uniquePaths(m: int, n: int) -> int:
    dp = [[1] * n for _ in range(m)]
    
    for row in range(1, m):
        for col in range(1, n):
            dp[row][col] = dp[row - 1][col] + dp[row][col - 1]
    
    return dp[m-1][n-1]

def uniquePathsSpaceOptimized(m: int, n: int) -> int:
    dp = [1] * n
    
    for row in (1, m):
        for col in range(1, n):
            dp[col] = dp[col] + dp[col - 1]
    
    return dp[n - 1]

while True:
    try:
        m = int(input("Please input the number of the rows of the matrix: "))
        break
    except ValueError:
        print("Please input a valid number.")
        
while True:
    try:
        n = int(input("Please input the number of the columns of the matrix: "))
        break
    except ValueError:
        print("Please input a valid number.")
        
pathCount = uniquePaths(m, n)
pathCountSpaceOptimized = uniquePathsSpaceOptimized(m, n)

print("The count of all possible unique path is: ", pathCount)
print("The count of all possible unique path counted by space optimized version is: ", pathCountSpaceOptimized)
    