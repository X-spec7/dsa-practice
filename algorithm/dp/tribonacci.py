class Solution:
    def __init__(self):
        self.memo = {}
        
    def tri(self, n: int) -> int:
        if n <= 0:
            return 0
        
        if n <= 2:
            return 1
        
        if n in self.memo:
            return self.memo[n]
        
        self.memo[n] = self.tri(n-1) + self.tri(n-2) + self.tri(n-3)
        
        return self.memo[n]
    
while True:
    try:
        n = int(input("Enter n: "))
        if n < 0:
            print("Input value should not be negative.")
            continue
        break
    except ValueError:
        print("Please input valid integer.")
    
sol = Solution()
print(sol.tri(n))