nums_1 = [2,3,5,6,7,8,9]
nums_2 = [1,3,4,5,7,10,12]
i = 0
j = 0

common_elements = []
while i < len(nums_1) and  j < len(nums_2):
    left = nums_1[i]
    right = nums_2[j]
    if left == right:
        common_elements.append(left)
        i += 1
        j += 1
    elif left < right:
        i += 1
    else:
        j += 1
print("common_elements:", common_elements)
