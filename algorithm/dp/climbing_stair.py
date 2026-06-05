class Solution:
    def __init__(self):
        self.memo = {}
        
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        if n in self.memo:
            return self.memo[n]
        
        self.memo[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        
        return self.memo[n]
    
while True:
    try:
        n = int(input("Enter n: "))
        if n <= 0:
            print("n must be a positive integer.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter an integer.")

sol = Solution()
print(sol.climbStairs(n))
