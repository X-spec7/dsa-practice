def deleteAndEarn(nums: list[int]) -> int:
    took_two_previous = 0
    took_one_previous = 0
    
    max_num = max(nums)
    
    points = [0] * (max_num + 1)
    
    for num in nums:
        points[num] += num
    
    for point in points:
        current = max(took_one_previous, took_two_previous + point)
        took_two_previous = took_one_previous
        took_one_previous = current
        
    return took_one_previous

while True:
    try:
        nums = list(map(int, input("Please input the array of numbers: ").split()))
        if not nums:
            print("Input array should not be empty")
            continue
        break
    except ValueError:
        print("Please input valid array of numbers!")
        
maxPoints = deleteAndEarn(nums)

print("The maximum points you can earn by delete and earn is: ", maxPoints)
