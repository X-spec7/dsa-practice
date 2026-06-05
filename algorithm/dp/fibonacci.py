class Solution:
    def __init__(self):
        self.memo = {}
        
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        
        if n in self.memo:
            return self.memo[n]
        
        self.memo[n] = self.fib(n-1) + self.fib(n-2)
        
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

print(sol.fib(n))