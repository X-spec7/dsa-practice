def triangleMinPath(dep: int, arr: list[list[int]]) -> int:
    if dep == 1:
        return arr[dep][0]
    
    for d in range(2, dep + 1):
        for i in range(d):
            if i == 0:
                arr[d - 1][i] += arr[d - 2][0]
            elif i == d - 1:
                arr[d - 1][i] += arr[d - 2][i - 1]
            else:
                arr[d - 1][i] += min(arr[d - 2][i - 1], arr[d - 2][i])
            
    return min(arr[dep - 1])
    

while True:
    try:
        dep = int(input("Input the depth of the triangle: "))
        
        if dep <= 0:
            print("The depth of the triangle should be positive.")
            continue
        break
    except ValueError:
        print("Please input the valid positive integer for the depth of triangle.")
        
arr = []
for i in range(dep):
    while True:
        try:
            row = list(map(int, input(f"Input the {i + 1}th row of the triangle.").split()))
            
            if len(row) != i + 1:
                print(f"The length of {i + 1}th row should be {i + 1}")
                continue
            
            if any(v <= 0 for v in row):
                print("Each value of each row should be positive integer.")
                continue
            
            arr.append(row)
            break
        except ValueError:
            print("Please input valid positive number array.")
            
result = triangleMinPath(dep, arr)

print("The minimum cost to reach the bottom is: ", result)