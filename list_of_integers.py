nums = input("Enter numbers separated by space (e.g. 45 120 99): ")
nums_list = [int(x) for x in nums.split()]
result = []

for i in nums_list:
    if i > 100:
        result.append("over")
    else:
        result.append(i)

print(result)
