class Solution:
    def find(self, nums: list[int], target: int) -> list[int]:
        seen = {0: -1}
        current_sum = 0
        
        for i, num in enumerate(nums):
            current_sum += num
            
            needed = current_sum - target
            
            if needed in seen:
                start = seen[needed] + 1
                end = i
                return nums[start:end + 1]
            
            seen[current_sum] = i
            
        return None

while True:
    try:
        nums = list(map(int, input("Enter array elements separated by spaces: ").split()))
        if not nums:
            print("Array cannot be empty")
        break
    except ValueError:
        print("Invalid input, please enter integers only.")
        
while True:
    try:
        target = int(input("Input the target number: "))
        break
    except ValueError:
        print("Invalid input. please enter an integer.")

sol = Solution()

result = sol.find(nums, target)

if result:
    print("Subarray found: ", result)
else:
    print("Subarray not found!")