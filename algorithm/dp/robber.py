class Solution:
    def rob(self, nums: list[int]) -> int:
        rob_one_before = 0
        rob_two_before = 0
        
        for num in nums:
            current = max(num + rob_two_before, rob_one_before)
            rob_two_before = rob_one_before
            rob_one_before = current
            
        return rob_one_before

while True:
    try:
        nums = list(map(int, input("Input the array of the money of each house: ").split()))
        if not nums:
            print("Input array cannot be empty!")
            continue
        break
    except ValueError:
        print("Please input valid number array!")
        
sol = Solution()

maxRob = sol.rob(nums)

print(f"I can steal up to {maxRob} tonight!")